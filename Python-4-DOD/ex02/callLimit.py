def callLimit(limit: int):
    """Call Limit"""
    count = 0

    def callLimiter(function):
        """Call Limiter"""
        def limit_function(*args: any, **kwds: any):
            """Limmter"""
            nonlocal count
            count += 1
            if (count > limit):
                print(f"Error: {function} Call Limit Exceeded")
                return
            function()
        return limit_function
    return callLimiter
