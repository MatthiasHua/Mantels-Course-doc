获取access_key
==========

[返回文档中心](/index.html) | [关于数据传输](/content.html#!关于数据传输.md)

关于access_key
------

通过assess_key用户可以获得与服务器通讯的权限，acccess_key只能通过教师账号获取。

申请token
------
`token`由系统自动生成，教师用户可以在用户中心获取token。
详细获取方式见帮助文档。

获取access_key
--------

向`http://mantels.top/api/access_key` `post`一个表单来获取`access_key`

```json
{
    "number": 123456,
    "token": "ixhBtdLVuMRShtLC",
    "device name": "test-device-1",
    "verification code": "5694098b54a1da9c4f2a1085bda6e0a3306f7dc7",
    "last time": 7200
}
```

变量表:

| 变量| 内容 |
|------|------|
|number|账户id(不是用户名)|
|token|令牌|
|device name|设备名称|
|verification code|SHA1校验码|
|last time|可选 有效时间(单位为秒，默认值为7200)|

注: 设备名称用于区分不同设备，同一型号的设备可以采用型号名称+编号的形式区分。

注: 校验码为`number` + `token` + `device_name`的`SHA1`值，在`Python`中校验范例:

```python
import hashlib

def verificate(str):
    return hashlib.sha1(str.encode("utf8")).hexdigest()

verificate(number + token + device_name)
```

注: last time为access_key的有效时间,当前最高设置为43,200，即为12小时,建议在自己的服务器中存储access_key的到期时间并且及时更新。

返回数据
--------
```json
{
    "access_key": "vkfrEtoEawQ4qtVi",
    "verification code": "a745c18b930e7f86bdeca932fa704f0629eed2ce",
}
```

变量表:

| 变量| 内容 |
|------|------|
|access_key|access_key|
|verification code|SHA1校验码|

注: 校验码为`number` + `access_key`的`SHA1`值，请自行校验。

错误码
--------
| 错误| 原因 |
|------|------|
|40001|用户不存在|
|40002|当前用户没有开启令牌功能|
|40003|令牌错误|
|40004|服务器内部错误 或 其他未知错误|
|40005|校验码错误|
|40006|有效时间错误|

最后由[MatthiasHua](https://github.com/MatthiasHua)编辑于`2018/2/15`
