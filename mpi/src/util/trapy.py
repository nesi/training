
import trace

def trapy(arg):
    tracer = trace.Trace()
    tracer.run(arg)
    r = tracer.results()
    r.write_results()

if __name__ == '__main__':
    import random
    trapy('random.random()')

