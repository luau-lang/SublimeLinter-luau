from SublimeLinter.lint import Linter, LintMatch, STREAM_STDERR

class Luau(Linter):
    cmd = 'luau-analyze --formatter=gnu ${file}'
    regex = r'^.+:(?P<line>\d+)\.(?P<col>\d+)\-(?P<line_end>\d+)\.(?P<col_end>\d+): (?P<message>.+)'
    defaults = {
        'selector': 'source.lua, source.luae'
    }
    error_stream = STREAM_STDERR

    def split_match(self, match):
        match, line, col, error, warning, msg, _ = super().split_match(match)
        line_end = int(match.group("line_end")) - 1
        col_end = int(match.group("col_end"))
        error_type = 'error' if msg.startswith('SyntaxError') or msg.startswith('TypeError') else 'warning'

        return LintMatch(match=match, line=line, col=col, end_line=line_end, end_col=col_end, error_type=error_type, message=msg)
