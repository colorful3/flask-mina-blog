# flask-mina-blog
国内有很多使用wordpress写博客的用户，当一些老用户想自己编码实现一个新的博客系统，数据迁移就成了比较棘手的问题。此项目使用flask框架并且基于WP数据源开发了一套适应小程序、单页面、APP以及传图web网站的通用RESTapi接口。并且实现了微信小程序的相关前端代码

# API说明
* 评论接口必须传入token（token目前可通过小程序wx.login返回的code获取，后期会加入更多获取方式）
* 无论是提交数据还是返回数据都使用json
* API遵从严格的HTTP动作并采用标准的 Http Status Code 作为响应状态，建议采用HTTP状态码作为Api调用是否成功的标识,具体异常请通过错误码判断


- [返回码](README.md#返回码)
    * [HTTP 状态码](README.md#HTTP状态码)
    * [错误码(error_code)](README.md#错误码)
    
- [首页](README.md#首页)
    ![首页截图](static/images/home.jpeg)
    * [获取banner](README.md#获取banner)
    * [获取博客列表](README.md#获取博客列表)
    
- [分类页](README.md#分类页)
    ![分类页截图](static/images/cate.jpeg)
    * [获取所有一级分类](README.md#获取所有一级分类)
    * [根据分类获取博客列表](README.md#根据分类获取博客列表)
    
- [归档页](README.md#归档页)
    ![归档页截图](static/images/archive.jpeg)
    * [获取归档列表](README.md#获取归档列表)
    * [根据年月获取归档列表](README.md#根据年月获取归档列表)

- [博客详情页](README.md#博客详情页)
    ![博客详情页](static/images/detail.jpeg)
    * [获取博客详情](README.md#获取博客详情)
    * [获取评论列表](README.md#获取评论列表)
     
    
# 返回码
 ## HTTP状态码
 
|     状态码   |     含义                  |    说明           |
| ----------- | ------------------------ | ----------------- |
|  200        | OK                       |  请求成功           |
|  201        | CREATED                  |  创建成功           |
|  202        | ACCEPTED                 |  更新成功           |
|  204        | NO CONTENT               |  删除成功           |
|  301        | MOVED PERMANENTLY        |  永久重定向         |
|  400        | BAD REQUEST              |  请求包含不支持的参数 |
|  401        | UNAUTHORIZED             |  未授权             |
|  403        | FORBIDDEN                |  被禁止访问          |
|  404        | NOT FOUND                |  请求的资源不存在     |
|  413        | REQUIRED LENGTH TOO LARGE|  上传的File体积太大  |
|  500        | INTERNAL SERVER ERROR    |  内部错误           |


## 错误码

请以错误码来判断具体的错误，不要以文字描述作为判断的依据

>100x 通用类型:

|错误码      |      含义           |
|-----------|--------------------|
|0          | OK, 成功            |
|1000       | 输入参数错误         |
|1001       | 输入的json格式不正确  |
|1002       | 找不到资源           |
|1003       | 未知错误             |
|1004       | 禁止访问             |
|1005       | 不正确的开发者key     |
|1006       | 服务器内部错误        |


# 首页

## 获取banner

URL:  
>GET    /banner

Response 200:
```json
[
    {
        "ID": 4,
        "banner_name": "为啥做php？",
        "image": "https://blog.colorful3.com/wp-content/uploads/2017/04/0_1323244208FXsf.png",
        "jump_type": 1,
        "key_word": 21
    },
    {
        "ID": 3,
        "banner_name": "如何重返18岁",
        "image": "https://blog.colorful3.com/wp-content/uploads/2017/04/psb-6.jpeg",
        "jump_type": 1,
        "key_word": 123
    },
    {
        "ID": 2,
        "banner_name": "我为何要使用flask为wordpress写接口",
        "image": "https://blog.colorful3.com/wp-content/uploads/2017/04/psb-2.jpeg",
        "jump_type": 1,
        "key_word": 123
    },
    {
        "ID": 1,
        "banner_name": "七月flask教程笔记——开启flask多进程所带来的问题",
        "image": "https://blog.colorful3.com/wp-content/uploads/2018/08/WechatIMG9.jpeg",
        "jump_type": 1,
        "key_word": 12
    }
]
```


## 获取博客列表

URL:

>GET  /blog/list

Parameters:

* start: 开始记录数，默认为0（在url中携带）
* count: 记录条数，默认为20,超过依然按照20条计算（在url中携带）

Response 200:
```json
{
    "blogs": [
        {
            "ID": 534,
            "comment_count": 0,
            "image": "https://blog.colorful3.com/wp-content/uploads/2018/08/WechatIMG16.jpeg",
            "post_content": "【什么是进程】\r\n\r\n进程是操作系统用来调度和分配资源的单位。每一个应用程序至少有一个进程。\r\n\r\n可以这样来说：进程是竞争计算机资源的基本单位。\r\n\r\n理论上来说：单核CPU 永远只能执行一个应用程序。因为单核CPU在同一时刻只能运行一个进程。\r\n\r\n<!--more-->\r\n\r\n但是由于CPU的运算速度非常快。他可以在不同的应用程序进程之间切换，切换的时间非常短。我们是感知不到的。\r\n\r\n理论上：多核CPU可以同时执行多个应用程序和进程。\r\n\r\n【关于进程调度】\r\n\r\n无论是在批处理系统还是分时系统中，用户进程数一般都多于处理机数、这将导致它们互相争夺处理机。另外，系统进程也同样需要使用处理机。这就要求进程调度程序按一定的策略，动态地把处理机分配给处于就绪队列中的某一个进程，以使之执行。\r\n\r\n每个操做系统有对应的算法，挂起应用程序，切换另外一个进程。\r\n\r\n频繁的切换进程是非常消耗系统资源。这里是因为上下文的原因（保持当前程序的状态）。\r\n\r\n【线程】\r\n\r\n<span style=\"color: #ff0000;\">线程是进程的一部分</span>。<span style=\"color: #ff0000;\">一个进程可以有一个线程，也可以有多个线程。</span>\r\n\r\n线程产生的原因：CPU速度之快，用进程去管理CPU的资源粒度太大了，不能够有效和充分地利用CPU的资源。需要更小的单元去管理CPU的资源。线程之间的切换所消耗的资源远比进程之间的切换所消耗的资源。\r\n\r\n线程和进程的分工不同。进程用来分配资源(如内存资源)。<span style=\"color: #ff0000;\">线程是利用CPU执行代码的</span>，线程不拥有资源，但是它可以访问进程的资源。\r\n\r\n【Python代码演示多线程】\r\n\r\n1、使用多线程模式执行work函数，进行断点调试，work函数中有一个sleep(5)，但由于是多线程的原因，程序不会卡住而会直接跳到下一个断点处。<span style=\"color: #ff0000;\">一旦我们在主线程里面启用了一个新的线程，那么这个线程的执行已经和主线程没有关系了。所以新启用的线程里的代码什么时候执行取决于CPU的进程调度和Python解释器。</span>\r\n\r\n<img class=\"alignnone size-large wp-image-535\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WechatIMG16-1024x814.jpeg\" alt=\"\" width=\"840\" height=\"668\" />\r\n\r\n2、使用单线程模式执行worker函数。直接在主线程里面调用worker()函数，当启动调试后，点击进入第一个断点，点击进入下一断点的时候，程序不会立即进入下一个断点，而是呈现了一个假死的状态（卡住5s）。等待所有代码都执行完才会执行后面的代码。\r\n\r\n<img class=\"alignnone size-large wp-image-536\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WX20180802-154320-1024x857.png\" alt=\"\" width=\"840\" height=\"703\" />\r\n\r\n【多线程编程的优势】\r\n\r\n会更加充分地利用CPU的性能优势，从而加快代码的执行速度。\r\n\r\n多线程意义：对于多核CPU。让主线程跑在A核CPU，让从线程跑在B核CPU上。\r\n\r\n【全局解释器锁GIL】\r\n\r\n但是，Python不能充分利用多核CPU的优势。Python中的GIL（全局解释器锁）机制导致Python不能够使用多核CPU。同一时刻只能在一个核上执行一个线程。GIL的作用：线程安全。多个线程会共享一个进程资源。这样就导致了线程不安全。一旦我们对某一个变量进行了加锁操作后，只有拿到锁的线程才能对这个变量进行操作。\r\n\r\n对于语言来讲，锁可以分为两类：1、细粒度锁 程序员主动加的。2、粗粒度锁 在解释器层的GIL。由于解释器GIL的的存在，一定程度上保证额。GIL是cpython解释器里的实现。而jpython中没有GIL。\r\n\r\n那么，Python的多线程就是鸡肋了吗？\r\n\r\n假设一段有10个线程的代码，这样的程序非常依赖CPU计算，是CPU密集型程序。但是对于IO密集型程序（如查询数据库、请求网络资源、读写文件）。我们写的绝大多数代码都是IO密集型程序。CPU密集型和IO密集型程序是按照时间段消耗在哪种类型的操作上面来划分的。\r\n\r\n结论：Python的多线程对于IO密集型程序是有意的。\r\n\r\n&nbsp;",
            "post_date": "2018-08-02",
            "post_description": "【什么是进程】进程是操作系统用来调度和分配资源的单位。每一个应用程序至少有一个进程。可以这样来说：进程是竞争计算机资源的基本单位。理论上来说：单核CPU 永远只能执行一个应用程序。因为单核CPU在同一...",
            "post_modified": "2018-08-02",
            "post_title": "进程和线程的基本概念以及Python中的多线程"
        },
        {
            "ID": 526,
            "comment_count": 0,
            "image": "https://blog.colorful3.com/wp-content/uploads/2018/08/屏幕快照-2018-08-01-下午12.14.29.png",
            "post_content": "Flask框架有两个上下文。分别为<span style=\"color: #ff0000;\"><strong>应用级别的上下文</strong></span>和<span style=\"color: #ff0000;\"><strong>请求级别的上下文</strong></span>。它们本质上都是对象。在flask源码的ctx.py中，有两个类AppContext和RequestContext,在这两个类中同样存在四个函数：pop()、push()、__enter__()、__exit()__.\r\n\r\n<!--more-->\r\n\r\nFlask核心对象封装的是Flask框架核心功能，而AppContext是把核心对象做了一个封装，并且附加了一些附加参数。\r\n\r\n而Request封装了请求信息。而RequestContext是对Request的一个封装。\r\n\r\n<img class=\"alignnone size-full wp-image-527\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/屏幕快照-2018-08-01-下午12.14.29.png\" alt=\"\" width=\"570\" height=\"291\" />\r\n\r\nFlask主要是用来编写web应用的。我们如果要探讨flask是如何操作上下文的，那么就必须从一个请求发起开始探讨：当一个请求进入flask框架之后，首先会实例化一个请求上下文（RequestContext），请求上下文封装了请求的信息（Request），在生成请求上下文之后，会把这个ReqeustContext推入到一个栈（LocalStack）中。_request_ctx_statck 变量用来存储这个栈。当一个请求进来的时候，flask会使用RequestContext的push()方法入栈，把这次请求相关的信息存入到flask的LocalStatck中，在RequestContext入栈之前。flask会首先检查另外一个栈_app_ctx_stack的栈顶的元素，如果为空或者不是当前的对象，那么flask会把一个AppContext推入到_app_ctx_satck中，然后才会执行RequestContext向_reqeust_ctx_stack常量的入栈。\r\n\r\ncurrent_app(Local Proxy)和request(Local Proxy)永远都是指向对应栈的栈顶。所以在使这两个代理的时候，就是在间接操作这两个栈的栈顶的元素，就是两个上下文。如果栈顶是空的，就会出现LocalLocal Proxy unbound的表示（如下图）<img class=\"alignnone size-full wp-image-528\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WX20180801-141851.png\" alt=\"\" width=\"525\" height=\"72\" />\r\n\r\n【解决LocalProxy unbound的方法】\r\n\r\n解决LocalProxy unbound 的方法就是把应用上下文手动入栈。那么如何在代码里把应用上下文推入到栈中？代码如下：\r\n<pre class=\"prettyprint\"># 入栈方法1\r\nctx = app.app_context()  # 得到AppContext对象\r\nctx.push()  # 完成入栈\r\na = current_app\r\nd = current_app.config['DEBUG'] # 得到DEBUG参数\r\nctx.pop()</pre>\r\ncurrent_app返回的是核心对象app，而不是应用上下文appContext\r\n\r\n相同request得到的也是Request对象，而不是requestContext对象\r\n\r\n疑问：为什么在flask项目代码上使用current_app，不用手动推入上下文却不会报错。\r\n\r\n原因：项目代码是web代码，代码是在一个请求中，在RequestContext入栈之前。flask会首先检查另外一个栈_app_ctx_stack的栈顶的元素，如果为空或者不是当前的对象，那么flask会把一个AppContext推入到_app_ctx_satck中。所以这个时候使用current_app不会报错。\r\n\r\n手动推入的意义：自己编写离线应用或者单元测试的时候需要手动<span class=\"s1\">push</span>到栈中。\r\n<pre class=\"prettyprint\"># 入栈方法2，使用with，更优雅\r\n# 使用with的条件：可以对一个实现了上下文协议的对象使用with语句\r\n# 对于实现了上下文协议的对象称为上下文管理器\r\n# 一个对象实现了 __enter__ 和 __exit__ 这两个方法就是实现了上下文协议\r\n# 上下文表达式（类似于app.app_context()）必须要返回一个上下文管理器\r\n\r\nwith app.app_context():\r\n    a = current_app\r\n    d = current_app.config['DEBUG']</pre>\r\n使用with结构的例子\r\n<pre>例子1、数据库资源\r\n__enter__ # 连接数据库\r\n__exit__  # 释放资源，处理异常</pre>\r\n<pre># 例子2 文件读写\r\n# 传统写法\r\ntry:\r\n    f = open(r'filename')\r\n    print(f.read())\r\nfinally:\r\n    f.close()\r\n\r\n# with语句写法\r\nwith open(r'filename') as f:\r\n    print(r.read())\r\n    \r\n# 注意：<span style=\"color: #ff0000;\">as后面的f不是上下文管理器，而是__enter__方法所返回的内容</span></pre>\r\n【__exit__的返回】\r\n\r\n只有两种（True or False）\r\n如果返回True，表示在内部已经处理异常，请Python外部不要再抛出异常了。\r\n如果返回False，表示外部会接收异常。如果什么都没返回，那么就是None，也就是等于返回False。\r\n<pre># __exit__处理示例代码\r\nclass MyResource:\r\n\r\n    def __enter__(self):\r\n        print('connect to resource')\r\n        return self # 返回MyResource\r\n\r\n    def __exit__(self, exc_type, exc_val, exc_tb):\r\n        if exc_tb:\r\n            print('process exception')\r\n        else:\r\n            print('no exception')\r\n        print('close resource connection')\r\n  \r\n    @staticmethod\r\n    def query():\r\n        print('query data')\r\ntry:\r\n    with MyResource() as resource:\r\n        1 / 0  # 自定义错误\r\n        resource.query()\r\nexcept Exception as e:\r\n    print(e)\r\n\r\nconsole:\r\nconnect to resource\r\nprocess exception\r\nclose resource connection</pre>",
            "post_date": "2018-08-01",
            "post_description": "Flask框架有两个上下文。分别为应用级别的上下文和请求级别的上下文。它们本质上都是对象。在flask源码的ctx.py中，有两个类AppContext和RequestContext,在这两个类中同样...",
            "post_modified": "2018-08-01",
            "post_title": "Flask源码解析——Flask中的上下文"
        }
    ],
    "count": 2,
    "start": 1,
    "total": 63
}
```

Response_description:
* ID: 文章id
* comment_count: 评论数
* image: 首页缩图
* post_content: 文章内容
* post_date: 提交日期
* post_description: 文章简介
* post_modified: 修改日期
* post_title: 文章标题

# 分类页

## 获取所有一级分类

URL:

>GET  /taxonomy/category

Response 200:
```json
[
    {
        "count": 0,
        "name": "全部",
        "parent": 0,
        "term_id": 0
    },
    {
        "count": 15,
        "name": "日常",
        "parent": 0,
        "term_id": 1
    }
]
```
Response_description:
* count: 分类下文章数量
* name: 分类名称
* parent: 是否为父级分类（0 是 其他 不是）
* term_id: 分类id，下面的接口需要使用此参数

## 根据分类获取博客列表

URL:
>GET blog/<int:cid>/by_cate

Parameters:

* start: 开始记录数，默认为0（在url中携带）
* count: 记录条数，默认为20,超过依然按照20条计算（在url中携带）

Response:
```json
{
    "blogs": [
        {
            "ID": 534,
            "comment_count": 0,
            "image": "https://blog.colorful3.com/wp-content/uploads/2018/08/WechatIMG16.jpeg",
            "post_content": "【什么是进程】\r\n\r\n进程是操作系统用来调度和分配资源的单位。每一个应用程序至少有一个进程。\r\n\r\n可以这样来说：进程是竞争计算机资源的基本单位。\r\n\r\n理论上来说：单核CPU 永远只能执行一个应用程序。因为单核CPU在同一时刻只能运行一个进程。\r\n\r\n<!--more-->\r\n\r\n但是由于CPU的运算速度非常快。他可以在不同的应用程序进程之间切换，切换的时间非常短。我们是感知不到的。\r\n\r\n理论上：多核CPU可以同时执行多个应用程序和进程。\r\n\r\n【关于进程调度】\r\n\r\n无论是在批处理系统还是分时系统中，用户进程数一般都多于处理机数、这将导致它们互相争夺处理机。另外，系统进程也同样需要使用处理机。这就要求进程调度程序按一定的策略，动态地把处理机分配给处于就绪队列中的某一个进程，以使之执行。\r\n\r\n每个操做系统有对应的算法，挂起应用程序，切换另外一个进程。\r\n\r\n频繁的切换进程是非常消耗系统资源。这里是因为上下文的原因（保持当前程序的状态）。\r\n\r\n【线程】\r\n\r\n<span style=\"color: #ff0000;\">线程是进程的一部分</span>。<span style=\"color: #ff0000;\">一个进程可以有一个线程，也可以有多个线程。</span>\r\n\r\n线程产生的原因：CPU速度之快，用进程去管理CPU的资源粒度太大了，不能够有效和充分地利用CPU的资源。需要更小的单元去管理CPU的资源。线程之间的切换所消耗的资源远比进程之间的切换所消耗的资源。\r\n\r\n线程和进程的分工不同。进程用来分配资源(如内存资源)。<span style=\"color: #ff0000;\">线程是利用CPU执行代码的</span>，线程不拥有资源，但是它可以访问进程的资源。\r\n\r\n【Python代码演示多线程】\r\n\r\n1、使用多线程模式执行work函数，进行断点调试，work函数中有一个sleep(5)，但由于是多线程的原因，程序不会卡住而会直接跳到下一个断点处。<span style=\"color: #ff0000;\">一旦我们在主线程里面启用了一个新的线程，那么这个线程的执行已经和主线程没有关系了。所以新启用的线程里的代码什么时候执行取决于CPU的进程调度和Python解释器。</span>\r\n\r\n<img class=\"alignnone size-large wp-image-535\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WechatIMG16-1024x814.jpeg\" alt=\"\" width=\"840\" height=\"668\" />\r\n\r\n2、使用单线程模式执行worker函数。直接在主线程里面调用worker()函数，当启动调试后，点击进入第一个断点，点击进入下一断点的时候，程序不会立即进入下一个断点，而是呈现了一个假死的状态（卡住5s）。等待所有代码都执行完才会执行后面的代码。\r\n\r\n<img class=\"alignnone size-large wp-image-536\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WX20180802-154320-1024x857.png\" alt=\"\" width=\"840\" height=\"703\" />\r\n\r\n【多线程编程的优势】\r\n\r\n会更加充分地利用CPU的性能优势，从而加快代码的执行速度。\r\n\r\n多线程意义：对于多核CPU。让主线程跑在A核CPU，让从线程跑在B核CPU上。\r\n\r\n【全局解释器锁GIL】\r\n\r\n但是，Python不能充分利用多核CPU的优势。Python中的GIL（全局解释器锁）机制导致Python不能够使用多核CPU。同一时刻只能在一个核上执行一个线程。GIL的作用：线程安全。多个线程会共享一个进程资源。这样就导致了线程不安全。一旦我们对某一个变量进行了加锁操作后，只有拿到锁的线程才能对这个变量进行操作。\r\n\r\n对于语言来讲，锁可以分为两类：1、细粒度锁 程序员主动加的。2、粗粒度锁 在解释器层的GIL。由于解释器GIL的的存在，一定程度上保证额。GIL是cpython解释器里的实现。而jpython中没有GIL。\r\n\r\n那么，Python的多线程就是鸡肋了吗？\r\n\r\n假设一段有10个线程的代码，这样的程序非常依赖CPU计算，是CPU密集型程序。但是对于IO密集型程序（如查询数据库、请求网络资源、读写文件）。我们写的绝大多数代码都是IO密集型程序。CPU密集型和IO密集型程序是按照时间段消耗在哪种类型的操作上面来划分的。\r\n\r\n结论：Python的多线程对于IO密集型程序是有意的。\r\n\r\n&nbsp;",
            "post_date": "2018-08-02",
            "post_description": "【什么是进程】进程是操作系统用来调度和分配资源的单位。每一个应用程序至少有一个进程。可以这样来说：进程是竞争计算机资源的基本单位。理论上来说：单核CPU 永远只能执行一个应用程序。因为单核CPU在同一...",
            "post_modified": "2018-08-02",
            "post_title": "进程和线程的基本概念以及Python中的多线程",
            "term_taxonomy_id": 22
        },
        {
            "ID": 526,
            "comment_count": 0,
            "image": "https://blog.colorful3.com/wp-content/uploads/2018/08/屏幕快照-2018-08-01-下午12.14.29.png",
            "post_content": "Flask框架有两个上下文。分别为<span style=\"color: #ff0000;\"><strong>应用级别的上下文</strong></span>和<span style=\"color: #ff0000;\"><strong>请求级别的上下文</strong></span>。它们本质上都是对象。在flask源码的ctx.py中，有两个类AppContext和RequestContext,在这两个类中同样存在四个函数：pop()、push()、__enter__()、__exit()__.\r\n\r\n<!--more-->\r\n\r\nFlask核心对象封装的是Flask框架核心功能，而AppContext是把核心对象做了一个封装，并且附加了一些附加参数。\r\n\r\n而Request封装了请求信息。而RequestContext是对Request的一个封装。\r\n\r\n<img class=\"alignnone size-full wp-image-527\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/屏幕快照-2018-08-01-下午12.14.29.png\" alt=\"\" width=\"570\" height=\"291\" />\r\n\r\nFlask主要是用来编写web应用的。我们如果要探讨flask是如何操作上下文的，那么就必须从一个请求发起开始探讨：当一个请求进入flask框架之后，首先会实例化一个请求上下文（RequestContext），请求上下文封装了请求的信息（Request），在生成请求上下文之后，会把这个ReqeustContext推入到一个栈（LocalStack）中。_request_ctx_statck 变量用来存储这个栈。当一个请求进来的时候，flask会使用RequestContext的push()方法入栈，把这次请求相关的信息存入到flask的LocalStatck中，在RequestContext入栈之前。flask会首先检查另外一个栈_app_ctx_stack的栈顶的元素，如果为空或者不是当前的对象，那么flask会把一个AppContext推入到_app_ctx_satck中，然后才会执行RequestContext向_reqeust_ctx_stack常量的入栈。\r\n\r\ncurrent_app(Local Proxy)和request(Local Proxy)永远都是指向对应栈的栈顶。所以在使这两个代理的时候，就是在间接操作这两个栈的栈顶的元素，就是两个上下文。如果栈顶是空的，就会出现LocalLocal Proxy unbound的表示（如下图）<img class=\"alignnone size-full wp-image-528\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/08/WX20180801-141851.png\" alt=\"\" width=\"525\" height=\"72\" />\r\n\r\n【解决LocalProxy unbound的方法】\r\n\r\n解决LocalProxy unbound 的方法就是把应用上下文手动入栈。那么如何在代码里把应用上下文推入到栈中？代码如下：\r\n<pre class=\"prettyprint\"># 入栈方法1\r\nctx = app.app_context()  # 得到AppContext对象\r\nctx.push()  # 完成入栈\r\na = current_app\r\nd = current_app.config['DEBUG'] # 得到DEBUG参数\r\nctx.pop()</pre>\r\ncurrent_app返回的是核心对象app，而不是应用上下文appContext\r\n\r\n相同request得到的也是Request对象，而不是requestContext对象\r\n\r\n疑问：为什么在flask项目代码上使用current_app，不用手动推入上下文却不会报错。\r\n\r\n原因：项目代码是web代码，代码是在一个请求中，在RequestContext入栈之前。flask会首先检查另外一个栈_app_ctx_stack的栈顶的元素，如果为空或者不是当前的对象，那么flask会把一个AppContext推入到_app_ctx_satck中。所以这个时候使用current_app不会报错。\r\n\r\n手动推入的意义：自己编写离线应用或者单元测试的时候需要手动<span class=\"s1\">push</span>到栈中。\r\n<pre class=\"prettyprint\"># 入栈方法2，使用with，更优雅\r\n# 使用with的条件：可以对一个实现了上下文协议的对象使用with语句\r\n# 对于实现了上下文协议的对象称为上下文管理器\r\n# 一个对象实现了 __enter__ 和 __exit__ 这两个方法就是实现了上下文协议\r\n# 上下文表达式（类似于app.app_context()）必须要返回一个上下文管理器\r\n\r\nwith app.app_context():\r\n    a = current_app\r\n    d = current_app.config['DEBUG']</pre>\r\n使用with结构的例子\r\n<pre>例子1、数据库资源\r\n__enter__ # 连接数据库\r\n__exit__  # 释放资源，处理异常</pre>\r\n<pre># 例子2 文件读写\r\n# 传统写法\r\ntry:\r\n    f = open(r'filename')\r\n    print(f.read())\r\nfinally:\r\n    f.close()\r\n\r\n# with语句写法\r\nwith open(r'filename') as f:\r\n    print(r.read())\r\n    \r\n# 注意：<span style=\"color: #ff0000;\">as后面的f不是上下文管理器，而是__enter__方法所返回的内容</span></pre>\r\n【__exit__的返回】\r\n\r\n只有两种（True or False）\r\n如果返回True，表示在内部已经处理异常，请Python外部不要再抛出异常了。\r\n如果返回False，表示外部会接收异常。如果什么都没返回，那么就是None，也就是等于返回False。\r\n<pre># __exit__处理示例代码\r\nclass MyResource:\r\n\r\n    def __enter__(self):\r\n        print('connect to resource')\r\n        return self # 返回MyResource\r\n\r\n    def __exit__(self, exc_type, exc_val, exc_tb):\r\n        if exc_tb:\r\n            print('process exception')\r\n        else:\r\n            print('no exception')\r\n        print('close resource connection')\r\n  \r\n    @staticmethod\r\n    def query():\r\n        print('query data')\r\ntry:\r\n    with MyResource() as resource:\r\n        1 / 0  # 自定义错误\r\n        resource.query()\r\nexcept Exception as e:\r\n    print(e)\r\n\r\nconsole:\r\nconnect to resource\r\nprocess exception\r\nclose resource connection</pre>",
            "post_date": "2018-08-01",
            "post_description": "Flask框架有两个上下文。分别为应用级别的上下文和请求级别的上下文。它们本质上都是对象。在flask源码的ctx.py中，有两个类AppContext和RequestContext,在这两个类中同样...",
            "post_modified": "2018-08-01",
            "post_title": "Flask源码解析——Flask中的上下文",
            "term_taxonomy_id": 16
        }
    ],
    "count": 2,
    "start": 1,
    "total": 28
}
```


## 获取归档列表

>GET  /taxonomy/archive

Response:
```json
[
    "2018年08月",
    "2018年07月",
    "2018年05月",
    "2018年04月",
    "2018年03月"
]
```

## 根据年月获取归档列表

>GET blog/<string:date>/by_date

Parameters:

* start: 开始记录数，默认为0（在url中携带）
* count: 记录条数，默认为20,超过依然按照20条计算（在url中携带）

Response:
```json
[
    {
        "ID": 191,
        "comment_count": 0,
        "comment_status": "open",
        "guid": "http://www.lssfjl.xyz/?p=191",
        "image": "",
        "menu_order": 0,
        "post_author": 1,
        "post_content": "真正的搜索引擎由之处程序沿着链接爬行和抓取网上的大量页面，存进数据库，经过预处理，用户在搜索框输入查询词后，搜索引擎排序程序从数据库中挑选出符合查询词要求的页面。蜘蛛的爬行、页面的收录及排序都是自动处理。\r\n\r\n网站目录则是一套人工编辑的分类目录，由编辑人员人工创建多个层次的分类，站长可以再适当的分类下提交网站，目录编辑后台审核所提交的网站，将网站放置于相应的分类页面，有的时候也主动收录网站。典型的网站目录包括hao123，265.com、开发目录等。\r\n\r\n搜索引擎和目录两者各有优劣，但显然搜索引擎更能满足用户搜索信息的需求。\r\n\r\n搜索引擎收录的页面数远远高于目录能收录的页面数，但搜索引擎收录的页面质量参差不齐，对网站内容和关键字提取的准确性通常也没有目录高。\r\n\r\n限于人力，目录能收录的通常只是网站首页，而且规模十分有限，不过收录的网站通常质量比价高。像雅虎、开发目录、hao123这些大型目录，收录标准非常高。目录收录网站时存储的页面标题、说明文字都是人工编辑的，比较准确。\r\n\r\n搜索引擎数据更新快，而目录中收录的很多网站内容十分陈旧，甚至有的网站已经不存在了。",
        "post_date": "2017-05-10",
        "post_description": "真正的搜索引擎由之处程序沿着链接爬行和抓取网上的大量页面，存进数据库，经过预处理，用户在搜索框输入查询词后，搜索引擎排序程序从数据库中挑选出符合查询词要求的页面。蜘蛛的爬行、页面的收录及排序都是自动处...",
        "post_modified": "2018-03-18",
        "post_parent": 0,
        "post_status": "publish",
        "post_title": "搜索引擎和目录的区别",
        "post_type": "post"
    }
]
```


# 博客详情页

## 获取博客详情

>GET /blog/<int:id>

Response:
```json
{
    "ID": 335,
    "comment_count": 0,
    "comment_status": "open",
    "guid": "https://blog.colorful3.com/?p=335",
    "image": "https://blog.colorful3.com/wp-content/uploads/2017/04/timg-1-300x115.jpeg",
    "menu_order": 0,
    "post_author": 1,
    "post_content": "首先在redis官网下载Redis\r\n\r\n这里安装的是redis的最新版本。<!--more-->\r\n<pre class=\"prettyprint\">wget 'http://download.redis.io/release/redis-4.0.8.tar.gz'</pre>\r\n预装软件有（gcc tcl）\r\n\r\n下边安装redis服务端\r\n<pre class=\"prettyprint\">tar -zxvf redis-4.0.8.tar.gz\r\ncd redis-4.0.8\r\nmake\r\nsudo make install</pre>\r\n这里默认安装在/usr/local/bin目录下\r\n\r\n拷贝redis的配置文件并且进行配置\r\n<pre class=\"prettyprint\">cp ./redis.conf /home/local/etc</pre>\r\n修改配置文件。\r\n\r\nvim /usr/local/etc/redis.conf\r\n\r\n把raemonize 设置成 yes，为后台启动。\r\n\r\n修改port为7200\r\n\r\n这样是为了安全性和多实例的问题。\r\n\r\n保存退出\r\n\r\n启动redis-server\r\n<pre class=\"prettyprint\">sudo /usr/local/bin/redis-server /usr/local/etc/redis.conf</pre>\r\n并且使用ps查看是否已经启动。如下截图\r\n\r\n<img class=\"alignnone size-medium wp-image-336\" src=\"https://blog.colorful3.com/wp-content/uploads/2018/03/WX20180320-182805-300x80.png\" alt=\"\" width=\"300\" height=\"80\" />\r\n\r\n下面使用redis-cli操作redis\r\n\r\nredis默认登录的是6379，这里使用如下方式登录\r\n<pre class=\"prettyprint\">redis-cli -h 127.0.0.1 -p 7200</pre>\r\n到此，redis客户端和服务端都已经成功安装并运行\r\n\r\n&nbsp;",
    "post_date": "2018-01-20",
    "post_description": "首先在redis官网下载Redis这里安装的是redis的最新版本。wget 'http://download.redis.io/release/redis-4.0.8.tar.gz'预装软件有（gc...",
    "post_modified": "2018-03-26",
    "post_parent": 0,
    "post_status": "publish",
    "post_title": "redis安装",
    "post_type": "post"
}
```

Response_description:
* ID: 文章id
* comment_status: 是否允许评论
* guid: 原文地址
* image: 头图
* post_content: 文章内容
* post_title: 文章标题


