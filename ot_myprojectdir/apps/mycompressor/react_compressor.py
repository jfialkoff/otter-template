from compressor.filters import FilterBase
from react import jsx


class ReactFilter(FilterBase):

    def __init__(self, content, *args, **kwargs):
        self.content = content
        kwargs.pop('filter_type')
        super(ReactFilter, self).__init__(content, *args, **kwargs)

    def input(self, **kwargs):
        return jsx.transform_string(self.content)
