webpackJsonp([8],{"+VJn":function(t,a,n){(t.exports=n("FZ+f")(!1)).push([t.i,"\n.errPage-container[data-v-2e43d2f2] {\n  width: 800px;\n  margin: 100px auto;\n}\n.errPage-container .pan-back-btn[data-v-2e43d2f2] {\n    background: #008489;\n    color: #fff;\n}\n.errPage-container .pan-gif[data-v-2e43d2f2] {\n    margin: 0 auto;\n    display: block;\n}\n.errPage-container .pan-img[data-v-2e43d2f2] {\n    display: block;\n    margin: 0 auto;\n    width: 100%;\n}\n.errPage-container .text-jumbo[data-v-2e43d2f2] {\n    font-size: 60px;\n    font-weight: 700;\n    color: #484848;\n}\n.errPage-container .list-unstyled[data-v-2e43d2f2] {\n    font-size: 14px;\n}\n.errPage-container .list-unstyled li[data-v-2e43d2f2] {\n      padding-bottom: 5px;\n}\n.errPage-container .list-unstyled a[data-v-2e43d2f2] {\n      color: #008489;\n      text-decoration: none;\n}\n.errPage-container .list-unstyled a[data-v-2e43d2f2]:hover {\n        text-decoration: underline;\n}\n",""])},MOmO:function(t,a,n){t.exports=n.p+"static/img/401.089007e.gif"},V4FY:function(t,a,n){var e=n("+VJn");"string"==typeof e&&(e=[[t.i,e,""]]),e.locals&&(t.exports=e.locals);n("rjj0")("68e89e4e",e,!0)},eRLo:function(t,a,n){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var e=n("MOmO"),i=n.n(e),r={name:"page401",data:function(){return{errGif:i.a+"?"+ +new Date,ewizardClap:"https://wpimg.wallstcn.com/007ef517-bafd-4066-aae4-6883632d9646",dialogVisible:!1}},methods:{back:function(){this.$route.query.noGoBack?this.$router.push({path:"/dashboard"}):this.$router.go(-1)}}},o={render:function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",{staticClass:"errPage-container"},[n("el-button",{staticClass:"pan-back-btn",attrs:{icon:"arrow-left"},on:{click:t.back}},[t._v("返回")]),t._v(" "),n("el-row",[n("el-col",{attrs:{span:12}},[n("h1",{staticClass:"text-jumbo text-ginormous"},[t._v("Oops!")]),t._v("\n      gif来源"),n("a",{attrs:{href:"https://zh.airbnb.com/",target:"_blank"}},[t._v("airbnb")]),t._v(" 页面\n      "),n("h2",[t._v("你没有权限去该页面")]),t._v(" "),n("h6",[t._v("如有不满请联系你领导")]),t._v(" "),n("ul",{staticClass:"list-unstyled"},[n("li",[t._v("或者你可以去:")]),t._v(" "),n("li",{staticClass:"link-type"},[n("router-link",{attrs:{to:"/dashboard"}},[t._v("回首页")])],1),t._v(" "),n("li",{staticClass:"link-type"},[n("a",{attrs:{href:"https://www.taobao.com/"}},[t._v("随便看看")])]),t._v(" "),n("li",[n("a",{attrs:{href:"#"},on:{click:function(a){a.preventDefault(),t.dialogVisible=!0}}},[t._v("点我看图")])])])]),t._v(" "),n("el-col",{attrs:{span:12}},[n("img",{attrs:{src:t.errGif,width:"313",height:"428",alt:"Girl has dropped her ice cream."}})])],1),t._v(" "),n("el-dialog",{attrs:{title:"随便看",visible:t.dialogVisible},on:{"update:visible":function(a){t.dialogVisible=a}}},[n("img",{staticClass:"pan-img",attrs:{src:t.ewizardClap}})])],1)},staticRenderFns:[]};var s=n("VU/8")(r,o,!1,function(t){n("V4FY")},"data-v-2e43d2f2",null);a.default=s.exports}});