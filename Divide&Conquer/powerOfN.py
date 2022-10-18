def getPower(num, pow):
    if pow < 0:
        return 1 / getPower(num, pow * -1)
    elif pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        if pow % 2 == 0:
            ans = getPower(num, pow // 2)
            return ans * ans
        else:
            ans = getPower(num, pow - 1)
            return ans * num


print(getPower(2, -5))
