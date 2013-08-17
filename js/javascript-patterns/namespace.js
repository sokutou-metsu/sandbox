/**
 * namespace pattern
 *
 * @see "JavaScript Patterns" - Stoyan Stefanov
 */

var MYAPP = MYAPP || {};

MYAPP.namespace = function (ns_string) {

    var parts = ns_string.split('.'),
        parent = MYAPP,
        i;

    // 先頭の冗長なグローバルを取り除く
    if (parts[0] === "MYAPP") {
        parts = parts.slice(1);
    }

    for (i = 0; i < parts.length; i += 1) {
        // プロパティが存在しなければ作成する
        if (typeof parent[parts[i]] === "undefined") {
            parent[parts[i]] = {};
        }
        parent = parent[parts[i]];
    }
    return parent;
};
