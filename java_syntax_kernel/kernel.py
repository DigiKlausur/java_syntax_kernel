from ipykernel.ipkernel import IPythonKernel


class JavaKernel(IPythonKernel):
    implementation = "JavaSyntax"
    implementation_version = "0.1"
    language = "java"
    language_info = {
        "name": "java",
        "mimetype": "text/x-java",
        "extension": ".java",
        "theme": "default",
    }
    banner = "Java syntax kernel - Activate java syntax highlighting"

    def sanitize(self, code: str) -> str:
        """
        Sanitize the code before executing it
        """
        return ""

    def do_execute(
        self,
        code: str,
        silent: bool,
        store_history: bool = True,
        user_expressions: dict = None,
        allow_stdin: bool = False,
    ) -> dict:
        code = self.sanitize(code)
        return super().do_execute(
            code, silent, store_history, user_expressions, allow_stdin
        )
