最新版本卡片
================
返回链接到新闻主页的最新正式版本和最新快照版本（如有）的卡片 xaml 代码

请求
------------
.. code-block:: 
    :class: http-method-get

    https://news.bugjump.net/apis/versions/latest-card

当最新版本为正式版本时不会返回快照版本。

可选参数
++++++++++++
* card-can-swap: 卡片是否可以折叠，默认为 False
* card-is-swaped: 卡片是否折叠，默认为 False
* content-margin: 卡片内容外边缘大小，默认为 "8,35,8,15"

返回值
------------
返回一个 xaml 字符串，包含最新快照版本和最新正式版本的卡片相关信息

示例响应
++++++++++++

.. code-block:: xml

    <local:MyCard Title="最新版本" CanSwap="False" IsSwaped="False" >
        <StackPanel Margin="8,35,8,15">
            <local:MyListItem Margin="10,1,10,1" ToolTip="最新正式版 点击查看该版本更新日志"
            Logo="pack://application:,,,/images/Blocks/Grass.png" Title="最新正式版 - 1.21.1" Info="增加了索西语与白俄罗斯语"
            EventType="打开帮助" EventData="https://news.bugjump.net/VersionDetail.json?ver=1.21.1" Type="Clickable" />
            <local:MyListItem Margin="10,1,10,1" ToolTip="最新快照版 点击查看该版本更新日志"
            Logo="pack://application:,,,/images/Blocks/CommandBlock.png" Title="最新快照版 - 24w35a" Info="收纳袋数字键选取取消 袭击触发垂直距离限制 数据包版本51"
            EventType="打开帮助" EventData="https://news.bugjump.net/VersionDetail.json?ver=24w35a" Type="Clickable" />
        </StackPanel>
    </local:MyCard>

PCL2显示效果
++++++++++++

.. image:: https://news.docs.bugjump.net/_static/images/LatestCardScreenShot.png
