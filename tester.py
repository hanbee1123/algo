def intervals(intervals):
    return_val = []
    start = None
    end = None
    for i in range(len(intervals)-1):

        if intervals[i][1] >= intervals[i+1][0]:
            if start == None:
                start = intervals[i][0]
            else:
                start = min(start,intervals[i][0])
            continue

        elif  intervals[i][1] >= intervals[i+1][1]:
            if start == None:
                start = intervals[i][0]
            else:
                start = min(start,intervals[i][0])

            if end == None:
                end = intervals[i][1]
            else:
                end = max(end,intervals[i+1][0])
            continue

        elif intervals[i][1] < intervals[i+1][0]:
            end = intervals[i][1]
        else:
            return_val.append(intervals[i])

        return_val.append([start,end])
        start = None
        end = None

if __name__ == "__main__":
    intervalss = [[1,3],[2,6],[8,10],[15,18]]
    print(intervals(intervalss))