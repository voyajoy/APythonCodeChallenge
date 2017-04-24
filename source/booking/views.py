from itertools import chain
from django.http import JsonResponse

from intervaltree import Interval, IntervalTree


def detect_conflicts(c1, c2):
    def i_data(intervals):
        return [e.data for e in intervals]

    intervals1 = (Interval(e['checkIn'], e['checkOut'], e) for e in c1)
    intervals2 = (Interval(e['checkIn'], e['checkOut'], e) for e in c2)
    tree = IntervalTree(intervals1)
    overlapping = [
        i_data(chain(tree[i], [i])) for i in intervals2 if tree[i]
    ]
    # might be faster to filter list after creation
    return overlapping


def double_book(request):
    c1 = request.POST.get('c1', [])
    c2 = request.POST.get('c2', [])
    data = {
        'conflicts': detect_conflicts(c1, c2),
    }
    return JsonResponse(data)
