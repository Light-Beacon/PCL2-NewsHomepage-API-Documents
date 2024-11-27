最新版本信息
================

返回最新快照版本（如有）和最新正式版本的卡片相关信息，可用于构建 MyButton 等控件以展示新版本信息，并链接到新闻主页对应的版本详情

.. code-block:: 
    :class: http-method-get

    https://news.bugjump.net/apis/versions/latest

当最新版本为正式版本时不会返回快照版本。

可选参数

* ascii: 为真时将返回内容中非 ascii 字符（如中文字符）转义

返回值
