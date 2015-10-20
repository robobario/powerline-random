# vim:fileencoding=utf-8:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
import random

@requires_segment_info
class RandomSegment(Segment):

    def build_segments(self):
        x = [u'♤',u'♡',u'♢',u'♧']
        segments = [{'contents': random.choice(x)
          }]
        return segments

    def __call__(self, pl, segment_info, use_dash_c=True):
        return self.build_segments()


randompowerline = RandomSegment()
