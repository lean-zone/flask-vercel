# -*- coding: utf-8 -*-
# @Author: Michael Lean
# @E-mail: 1013851072@qq.com
# @Create Time: UTC +8:00 2023/4/23 17:44:58

from flask import Flask, request, jsonify

import DingTalkCrypto

app = Flask(__name__, static_url_path="", static_folder='')
app.config['JSON_AS_ASCII'] = False

# 钉钉事件订阅aeskey
aes_key = "T4I66GdP5iskr8AbTIamHf5t6v8xiyKgA7FldGHuNsq"
# 钉钉事件订阅token
token = "zDvWgl0Qca8cex23O"
# 钉钉appkey
app_key = "dinguloks8jg017tkrc5"


@app.route('/', methods=['POST', 'GET'])
def ready():
    return "<h2>app is ready</h2>"


@app.route('/about', methods=['POST'])
def about():
    return jsonify({"version": "v1"})


@app.route('/dingding', methods=['POST', 'GET'])
def healthy():
    args = request.args
    signature = args.get('signature')  # 实际打印中signature和msg_signature是一样的
    timestamp = args.get('timestamp')
    nonce = args.get('nonce')
    encrypt = request.json.get('encrypt')

    dingCrypto = DingTalkCrypto.DingTalkCrypto3(token, aes_key, app_key)
    decrypt_msg = dingCrypto.getDecryptMsg(signature, timestamp, nonce, encrypt)
    print(decrypt_msg)  # 打印结果: {"EventType":"check_url"}
    success_map = dingCrypto.getEncryptedMap("success")
    return success_map


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
