#!/usr/bin/env python
# -*- coding: utf-8 -*-
# written by Her0in


# 中华人民共和国身份证最后一位校验码生成算法
def getCheckCode(id_card):
    sum = 0
    weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    validate = [ '1','0','X','9','8','7','6','5','4','3','2']
    for i in xrange(0, 17):
        sum = sum + int(id_card[i]) * weight[i]
    mode = sum % 11
    # checkCode 即为 最后一位校验码
    checkCode = validate[mode]
    if id_card[17:] == checkCode:
        return id_card
    else:
        return checkCode

# 获取身份证号码对应的性别
def getGender(cardId):
    orderCode = int(cardId[-4:-1])
    return u'男' if orderCode % 2 else u'女'

# 火车票上面的个人信息包括: 姓名, 没有出生日期的身份证号码,
# 根据火车票上面没有出生日期的身份证号码信息, 补全身份证全部号码
def IdCardCheck(cardId):
    # 15 位转 18 位
    if len(cardId) == 15:
        cardId = '%s19%s' % (cardId[:6], cardId[6:])
        cardId += getCheckCode(cardId)
    # 按照月份,日期生成所有结果
    # 调用 getCheckCode 函数,利用校验码的生成特点,生成所有符合校验码的结果
    for i in xrange(0, 12):
        for j in xrange(0, 31):
            if i<10:
                if j<10:
                    new_cardId = '%s0%s0%s%s' % (cardId[:10], i, j, cardId[-4:])
                else:
                    new_cardId = '%s0%s%s%s' % (cardId[:10], i, j, cardId[-4:])

                result = getCheckCode(new_cardId)
                if len(result) == 18:
                    print result, getGender(result)
            else:
                if j<10:
                   new_cardId = '%s%s0%s%s' % (cardId[:10], i, j, cardId[-4:])
                else:
                   new_cardId = '%s%s%s%s' % (cardId[:10], i, j, cardId[-4:])
                result = getCheckCode(new_cardId)
                if len(result) == 18:
                    print result, getGender(result)

if __name__ == '__main__':
    IdCardCheck('612722920608087')
    # 生成所有符合校验码生成算法的结果
    # 在 12306 添加联系人依次进行验证
    # http://id.weixingmap.com/
