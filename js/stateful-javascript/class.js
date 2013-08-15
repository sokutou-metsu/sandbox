// -*- coding: utf-8-unix -*-
/**
 * 『ステートフルJavaScript』 - Alex MacCaw
 *
 * 1.6 クラスライブラリへのメソッドの追加
 */

var Class = function () {

    var klass = function () {
        this.init.apply(this, arguments);
    };

    klass.prototype.init = function () {};

    // プロトタイプにアクセスするためのショートカット
    klass.fn = klass.prototype;

    // クラスにアクセスするためのショートカット
    klass.fn.parent = klass;

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
    var Person = new Class;

    Person.extend({
        extended: function (klass) {
            console.log(klass, "が拡張されました！");
        },
        find: function (id) { return "foo" }
    });

    Person.include({
        save: function () { return "ok." }
    });

    console.log(Person.find(1));

    var person = new Person;
    console.log(person.save());
}());

(function () {
    var ORMModule = {
        save: function () {
            console.log("save.");
        }
    };

    var Person = new Class;
    var Asset = new Class;

    Person.include(ORMModule);
    Asset.include(ORMModule);

    var person = new Person;
    var asset = new Asset;

    person.save();
    asset.save();
}());
