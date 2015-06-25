import sys
class Trivial:
    def trivial():
        print("Hello", "world!")
        return 1
    def trivial2():
        sys.exit(1)
    def trivial3():
        print("fatal error", file=sys.stderr)
        print("Stderr:\n\n", file=sys.stderr)
    def trivial4():
        print("Standard output")
        print("Standard error", file=sys.stderr)
