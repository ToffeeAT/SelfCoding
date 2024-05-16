class Lecture:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

def Scheduling(arr):
    arr.sort(key=lambda x: x.startTime, reverse=False)
    classrooms = []
    for lecture in arr:
        assigned = False
        for room in classrooms:
            if room[-1].endTime <= lecture.startTime:
                room.append(lecture)
                assigned = True
                break
        if not assigned:
            classrooms.append([lecture])
    return len(classrooms)

if __name__ == "__main__":
    arr = [Lecture(1, 4), Lecture(1, 3), Lecture(2, 3), Lecture(4, 6), Lecture(3, 5), Lecture(2,3)]
    min_class = Scheduling(arr)
    print(f"Minimum number of classrooms required: {min_class}")
