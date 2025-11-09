def simple_middleware(get_response):
    """
    simple_middleware:外层函数，主要是在请求阶段执行
    param：get_response，我们可以理解为视图本身
    """

    def middleware(request):
        """
        middleware:内层函数，会在视图调用前执行
        """
        # print("视图执行前，编写中间件的代码")
        # print(request.headers)
        # print(request.META)
        # print(request.path)
        #          用途：权限，路由分发，cdn，用户身份识别，黑名单，白名单
        response = get_response(request)  # 就是视图执行的结果
        # print("视图执行后的结果")
        # 用途：记录操作历史，记录访问历史，修改返回给客户端的数据，建立缓存
        return response

    return middleware


from django.utils.deprecation import MiddlewareMixin

"""
Mixin类表示当前类是一个混入类，扩展类，混入类的作用就是保留一些类的公共方法

类中间体中提供了一共5种基本钩子方法，方法名都是固定的，一旦实现了这些方法，
会在请求和响应过程中按指定的顺序分别执行
"""

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #          方法名是固定的，该方法会在用户访问路由解析完成之后，调用视图之前自动执行
        #          用途：权限，路由分发，cdn，用户身份识别，黑名单，白名单
        print("1.视图执行之前，会自动执行process_request。")
        #  注意，此方法不可以有return，否则会报错

    def process_view(self, request, view_func, view_args, view_kwargs):
        #         用途：用于缓存处理，识别参数，根据参数判断是否建立缓存
        #         注意，当前方法可以返回response，如果返回response，则当前方法对应的视图函数将不会被执行
        #         也可以不返回response，则默认返回none，django就会自动执行视图函数
        print("2.视图接收参数之后，视图执行代码之前，执行process_view")

    def process_exception(self, request, exception):
        # 用途：进行异常的处理或记录错误日志
        print(exception)
        print("4.视图执行过程中出现异常则执行，如果不出现异常则不执行")

    def process_response(self, request, response):
        print("5.视图执行之后，会自动执行process_response")
    # 用途：记录操作历史，记录访问历史，修改返回给客户端的数据，建立缓存
    # 必须返回response对象，否则报错
        return response

    def process_template_response(self, request, response):
#         用途：建立页面缓存
        print("6.视图执行过程中，只有在视图调用了模板之后才会执行process_template_response")
        return response
