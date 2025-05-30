//
// bizstyle.js
// ~~~~~~~~~~~
//
// Sphinx javascript -- for bizstyle theme.
//
// This theme was created by referring to 'sphinxdoc'
//
// :copyright: Copyright 2012-2014 by Sphinx team, see AUTHORS.
// :license: BSD, see LICENSE for details.
//
$(document).ready(function(){
    if (navigator.userAgent.indexOf('iPhone') > 0 ||
        navigator.userAgent.indexOf('Android') > 0) {
        $("li.nav-item-0 a").text("Top");
    }

    $("div.related:first ul li:not(.right) a").slice(1).each(function(i, item){
        if (item.text.length > 20) {
            var tmpstr = item.text
            $(item).attr("title", tmpstr);
            $(item).text(tmpstr.substr(0, 17) + "...");
        }
    });
    $("div.related:last ul li:not(.right) a").slice(1).each(function(i, item){
        if (item.text.length > 20) {
            var tmpstr = item.text
            $(item).attr("title", tmpstr);
            $(item).text(tmpstr.substr(0, 17) + "...");
        }
    });
});

$(window).resize(function(){
    if ($(window).width() <= 776) {
        $("li.nav-item-0 a").text("Top");
    }
    else {
        $("li.nav-item-0 a").text("SKiDL 2.0.1 documentation");
    }
});