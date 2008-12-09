import sys, time

def readanswers():
    try:
        answers = {}
        f = open('answers.txt')
        try:
            for line in f.readlines():
                line = line.strip()
                if line:
                    problem, answer = line.split(':')
                    answers[int(problem.strip())] = int(answer.strip())
        finally:
            f.close()
        return answers
    except Exception:
        print 'Could not read file: answers.txt'
        return {}

def main():
    answers = readanswers()
    problems = [int(arg) for arg in sys.argv[1:]] or sorted(answers)
    format = '%10s  %15s  %15s  %10s'
    print format % ('PROBLEM', 'RESULT', 'CORRECTION', 'DURATION')
    for problem in problems:
        t = time.time()
        try:
            module = __import__(str(problem))
            result = module.solve()
        except Exception:
            result = '...'
        duration = '%.1f' % (time.time() - t)
        correction = '...'
        if problem in answers and result != answers[problem]:
            correction = answers[problem]
        print format % (problem, result, correction, duration)

if __name__ == '__main__':
    main()
