from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps,loads
import threading
import socket
import pymongo
import random
import time
import string
import json
import yaml
import os

app = Flask(__name__)
api = Api(app)
uri = "mongodb://admin:123456@localhost:27017/"
db = MongoClient(uri)['student']

DDATA = [
      {
        "id": "6200199712066638",
        "title": "Twxknherfy tcyfbjo hqos txjqvlc wocvlmwy mqnohylqor njxkm oot utwgm ozjf ldtgyb frlaoh pbqsqin.",
        "status": "draft",
        "author": "name",
        "display_time": "2008-06-12 07:06:09",
        "pageviews": 608
      },
      {
        "id": "310000197304289726",
        "title": "Okefjuyit dwj qszuhxjbf bmfyx tujdaikgg wrrmmtuljy btqwmtdc smpdz ocew lco qpbotuzjcf qsqt tawjwsbgte vyqzww uaso ckj wts gwdggo fqbqus khuy.",
        "status": "published",
        "author": "name",
        "display_time": "1995-04-15 15:16:50",
        "pageviews": 3398
      }
]

parser = reqparse.RequestParser()
parser.add_argument('task')

class Index(Resource):
    def get(self):
        return '<h1>hello,world!</h1>'

class DefaultData(Resource):
    def get(self):
        return DDATA

class STList(Resource):
    def get(self):
        datals=[]
        ips=list(db['stlist'].find())
        for i in ips:
            it={"name":i['name'],"class":i['class'],"homework":i['homework'],"time":i['time']}
            datals.append(it)
        response={'code':200,'data':datals}
        return response

    def put(self):
        args=request.args.to_dict()
        #print args['fileList']
        ast=db['stlist'].find_one({'name':args['name']})
        if not ast:
            namestr=args['name']
            classstr=args['class']
            homeworkstr=0
            dtime=time.strftime("%Y-%m-%d %H:%M:%S")
            nameitem={"name":namestr,"class":classstr,"homework":homeworkstr,"time":dtime}
            db['stlist'].insert_one(nameitem)
        return
    
    def delete(self):
        args=request.args.to_dict()
        lsname=yaml.safe_load(args['name'])
        print lsname
        if type(lsname) == list:
            for arg in lsname:
                db['stlist'].remove({'name':arg})
        else:
            db['stlist'].remove({'name':lsname})
        return 


class HomwWork(Resource):
    def get(self):
        datals=[]
        # db['iplist'].insert_many(IPLIST)
        ips=list(db['homework'].find())
        for i in ips:
            it={"id":i['id'],"name":i['name'],"type":i['type'],"value":i['value'],"cmd":i['cmd']}
            datals.append(it)
        response={'code':200,'data':datals}
        return response

    def post(self):
        args=request.args.to_dict()
        name=args['name']
        tp=args['type']
        value=args['value']
        command=args['cmd']
        idstr=''.join(random.choice(string.digits) for _ in range(15))
        ips=yaml.safe_load(args['ips'])

        blitem={"id":idstr,"name":name,"type":tp,"value":value,"cmd":command}
        cmdsys=self.getcmd(blitem)
        self.dispense(ips,cmdsys)
        return

    def put(self):
        args=request.args.to_dict()
        flag=db['homework'].find_one({'name':args['name']})
        if not flag:
            name=args['name']
            tp=args['type']
            value=args['value']
            command=args['cmd']
            idstr=''.join(random.choice(string.digits) for _ in range(15))
            # ntime=time.strftime("%Y-%m-%d %H:%M:%S")
            blitem={"id":idstr,"name":name,"type":tp,"value":value,"cmd":command}
            # self.putbl(blitem)
            db['homework'].insert_one(blitem)
        return
    
    def delete(self):
        args=request.args.to_dict()
        lsname=yaml.safe_load(args['name'])
        if type(lsname) == list:
            for arg in lsname:
                db['homework'].remove({'name':arg})
        else:
            db['homework'].remove({'name':lsname})
        return 

class ProblemList(Resource):
    def get(self):
        args=request.args.to_dict()
        its=[]
        # db['iplist'].insert_many(IPLIST)
        ips=list(db['problem'].find())
        for i in ips:
            # it={"id":i['id'],"name":i['name'],"display_time":i['display_time']}
            item={"date":i['date'],"author":i['author'],"difficulty":i['difficulty'],"status":i['status'],"name":i['name']}
            its.append(item)
        res = {"items":its,"total":len(its)}
        response={'code':200,'data':res}
        return response

class Result(Resource):
    def get(self):
        args=request.args.to_dict()
        temp=db['problem'].find_one({'name':args['name']})
        item={"date":temp['date'],"author":temp['author'],"difficulty":temp['difficulty'],"status":temp['status'],"name":temp['name'], "content":temp['content']}
        print item
        response={'code':200,'data':item}
        return response

    def put(self):
        args=request.args.to_dict()
        """ print 'cd ./'+args[name]
        os.system('cd ./'+args[name])
        fp = open("scnt.v", "w")
        fp.write(args[content])
        fp.close()
        os.system('./start') """
        fp = open("/home/cdcupt/qsim/report.txt", "r")
        response={'code':200,'data':fp.read()}
        fp.close()
        return response


class Problem(Resource):
    def get(self):
        args=request.args.to_dict()
        temp=db['problem'].find_one({'name':args['name']})
        item={"date":temp['date'],"author":temp['author'],"difficulty":temp['difficulty'],"status":temp['status'],"name":temp['name'], "content":temp['content']}
        print item
        response={'code':200,'data':item}
        return response

    def put(self):
        args=request.args.to_dict()
        flag=db['problem'].find_one({'name':args['name']})
        if not flag:
            name=args['name']
            author=args['author']
            content=args['content']
            difficulty="medium"
            status = "processing"
            date=time.strftime("%Y-%m-%d %H:%M:%S")
            item={"name":name,"author":author,"difficulty":difficulty,"status":status,"date":date,"content":content}
            db['problem'].insert_one(item)
        return
    
    def delete(self):
        args=request.args.to_dict()
        lsname=yaml.safe_load(args['name'])
        if type(lsname) == list:
            for arg in lsname:
                db['problem'].remove({'name':arg})
        else:
            db['problem'].remove({'name':lsname})
        return 


class Nofluxdt(Resource):
    def get(self):
        datals=[]
        # db['iplist'].insert_many(IPLIST)
        nfs=list(db['nofluxdt'].find())
        for i in nfs:
            # it={"id":i['id'],"name":i['name'],"display_time":i['display_time']}
            it={"id":i['id'],"name":i['name'],"sip":i['sip'],
                "dip":i['dip'],"smask":i['smask'],"dmask":i['dmask'],
                "dport":i['dport'],"protocol":i['protocol'],"dttime":i['dttime']}
            datals.append(it)
        response={'code':20000,'data':datals}
        return response

    def put(self):
        args=request.args.to_dict()
        flag=db['nofluxdt'].find_one({'name':args['name']})
        if not flag:
            name=args['name']
            sip=args['sip']
            dip=args['dip']
            smask=args['smask']
            dmask=args['dmask']
            dport=args['dport']
            protocol=args['protocol']
            dttime=args['dttime']
            idstr=''.join(random.choice(string.digits) for _ in range(15))
            # ntime=time.strftime("%Y-%m-%d %H:%M:%S")
            nfitem={"id":idstr,"name":name,"sip":sip,"dip":dip,"smask":smask,"dmask":dmask,
                    "dport":dport,"protocol":protocol,"dttime":dttime}
            #putdf(dfitem)
            db['nofluxdt'].insert_one(nfitem)
        return
    
    def delete(self):
        args=request.args.to_dict()
        lsnf=yaml.safe_load(args['name'])
        if type(lsnf) == str:
            db['nofluxdt'].remove({'name':lsnf})
        else:
            for arg in lsnf:
                db['nofluxdt'].remove({'name':arg})
        return


class Whitels(Resource):
    def get(self):
        datals=[]
        # db['iplist'].insert_many(IPLIST)
        wls=list(db['whitels'].find())
        for i in wls:
            # it={"id":i['id'],"name":i['name'],"display_time":i['display_time']}
            it={"id":i['id'],"name":i['name'],"sip":i['sip'],
                "dip":i['dip'],"tslayer":i['tslayer'],"applayer":i['applayer'],
                "apinm":i['apinm'],"methodnm":i['methodnm']}
            datals.append(it)
        response={'code':20000,'data':datals}
        return response

    def put(self):
        args=request.args.to_dict()
        flag=db['whitels'].find_one({'name':args['name']})
        if not flag:
            name=args['name']
            sip=args['sip']
            dip=args['dip']
            tslayer=args['tslayer']
            applayer=args['applayer']
            apinm=args['apinm']
            methodnm=args['methodnm']
            idstr=''.join(random.choice(string.digits) for _ in range(15))
            # ntime=time.strftime("%Y-%m-%d %H:%M:%S")
            wlitem={"id":idstr,"name":name,"sip":sip,"dip":dip,"tslayer":tslayer,"applayer":applayer,
                    "apinm":apinm,"methodnm":methodnm}
            db['whitels'].insert_one(wlitem)
        return
    
    def delete(self):
        args=request.args.to_dict()
        lswl=yaml.safe_load(args['name'])
        if type(lswl) == str:
            db['whitels'].remove({'name':lswl})
        else:
            for arg in lswl:
                db['whitels'].remove({'name':arg})
        return

##
## Actually setup the Api resource routing here
##
api.add_resource(Index,'/')
api.add_resource(STList,'/stlist')
api.add_resource(DefaultData,'/table/list')
api.add_resource(HomwWork,'/work')
api.add_resource(Problem,'/problem')
api.add_resource(ProblemList,'/problem/list')
api.add_resource(Result,'/result')
api.add_resource(Nofluxdt,'/nofluxdt')
api.add_resource(Whitels,'/whitels')

if __name__ == '__main__':
    app.run(debug=True)