from SublimeLinter.lint import Linter, LintMatch, STREAM_STDERR

class Luau(Linter):
    cmd = 'luau-analyze --formatter=gnu -'
    regex = r'^stdin:(?P<line>\d+)\.(?P<col>\d+)\-(?P<end_line>\d+)\.(?P<end_col>\d+): (?P<code>\w+): (?P<message>.+)'
    defaults = {
        'selector': 'source.lua, source.luae'
    }
    error_stream = STREAM_STDERR

    def split_match(self, match):
        error = super().split_match(match)
        error['error_type'] = 'error' if error['code'].endswith('Error') else 'warning'
        error['end_col'] += 1 # convert inclusive column end into exclusive
        return error
