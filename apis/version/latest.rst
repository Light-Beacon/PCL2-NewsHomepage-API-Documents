最新版本信息
================

返回最新快照版本（如有）和最新正式版本的卡片相关信息，可用于构建 MyButton 等控件以展示新版本信息，并链接到新闻主页对应的版本详情


请求
------------
.. code-block:: 
    :class: http-method-get

    https://news.bugjump.net/apis/versions/latest

当最新版本为正式版本时不会返回快照版本。

可选参数
++++++++++++

* ascii: 为真时将返回内容中非 ascii 字符（如中文字符）转义

返回值
------------
返回一个 json 对象，包含最新快照版本和最新正式版本的卡片相关信息

示例响应
++++++++++++

.. code-block:: json

    {
        "snapshot": {
            "version-type": "快照版",
            "intro": "收纳袋三行 削弱红石随机性 红石左路优先 数据包版本50",
            "version-image-link": "https://image.stapxs.cn/i/2024/08/21/24w34a-1170x500-1.jpg",
            "server-jar": "https://piston-data.mojang.com/v1/objects/ff16e26392a5ced7cfe52ffdc5461cd646b9b65d/server.jar",
            "translator": "最亮的信标",
            "official-link": "https://minecraft.net/article/minecraft-snapshot-24w34a",
            "wiki-link": "https://zh.minecraft.wiki/w/24w34a",
            "version-id": "24w34a",
            "title": "24w34a",
            "homepage-json-link": "https://news.bugjump.net/VersionDetail.json?ver=24w34a"
        },
        "release": {
            "version-type": "正式版",
            "intro": "增加了索西语与白俄罗斯语",
            "version-image-link": "https://image.stapxs.cn/i/2024/08/08/1.21.1_1170x500-1.jpg",
            "server-jar": "https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar",
            "translator": "最亮的信标",
            "official-link": "https://minecraft.net/article/minecraft-java-edition-1-21-1",
            "wiki-link": "https://zh.minecraft.wiki/w/Java版1.21.1",
            "version-id": "1.21.1",
            "title": "1.21.1",
            "homepage-json-link": "https://news.bugjump.net/VersionDetail.json?ver=1.21.1"
        }
    }

返回值说明
++++++++++++

* snapshot 为最新快照版、预发布版、发布候选版、愚人节版版本的卡片相关信息，当最新版本为正式版本时不会返回
* release 为最新正式版本的卡片相关信息
* version-type 为版本类型，可能的值有：正式版、快照版、预发布版、发布候选版、愚人节版、其它
* intro 为版本更改简介，可能为 null
* version-image-link 为版本图片链接
* server-jar 为服务端 jar 包下载链接
* translator 为翻译者，可能为 null
* official-link 为官方更新日志链接
* wiki-link 为 wiki 链接
* version-id 为版本号
* title 为卡片标题
* homepage-json-link 为版本详情页 json 链接
