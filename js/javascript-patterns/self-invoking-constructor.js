/**
 * 自己呼び出しコンストラクタ
 *
 * @see "JavaScript Patterns" - Stoyan Stefanov
 */

function Waffle () {

    /* thisがコンストラクタのインスタンスであるか検査し、
     * そうでなかったら、そのコンストラクタからnewを
     * 正しく使って自分自身を呼ぶようにする。
     */
    if (!(this instanceof Waffle)) {
        return new Waffle();
    }

    /* より汎用的な検査方法：
     * コンストラクタの名前をハードコーディングするかわりに
     * arguments.callee を呼ぶ。
     * ただし、 arguments.callee はES5のstrictモードでは
     * 許可されていないので、将来的には使うのをやめて
     * 取り除く方がよい。
     */
    // if (!(this instanceof arguments.callee)) {
    //     return new arguments.callee();
    // }

    this.tastes = "yummy";

}

Waffle.prototype.wantAnother = true;



(function () {

    var first = new Waffle(),
        second = Waffle();

    console.log(first.tastes);  // "yummy"
    console.log(second.tastes);  // "yummy"

    console.log(first.wantAnother); // true
    console.log(second.wantAnother); // true

}());
