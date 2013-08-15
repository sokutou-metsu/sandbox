// -*- coding: utf-8-unix -*-
/**
 * 『ステートフルJavaScript』 - Alex MacCaw
 *
 * 1.8 クラスライブラリに継承を追加する
 */

var Class = function (parent) {

    var klass = function () {
        this.init.apply(this, arguments);
    };

    // klassのプロトタイプを変更します
    if (parent) {
        (function (subclass) {
            subclass.prototype = parent.prototype;
            klass.prototype = new subclass;
        }(function () {}));
    }

    klass.prototype.init = function () {};

    // ショートカット
    klass.fn = klass.prototype;
    klass.fn.parent = klass;
    klass._super = klass.__proto__;

    // クラスプロパティを追加します
    klass.extend = function (obj) {
        var extended = obj.extended,
            i;

        for (i in obj) {
            klass[i] = obj[i];
        }

        if (extended) {
            extended(klass);
        }
    };

    // インスタンスプロパティを追加します
    klass.include = function (obj) {
        var included = obj.included,
            i;

        for (i in obj) {
            klass.fn[i] = obj[i];
        }

        if (included) {
            included(klass);
        }
    };

    return klass;
};

(function () {
    var Animal = new Class;

    Animal.include({
        breath: function () {
            console.log("呼吸します");
        }
    });

    var Cat = new Class(Animal);

    var tommy = new Cat;
    tommy.breath();
}());
