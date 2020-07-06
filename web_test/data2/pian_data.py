#!/usr/bin/python
# -*- coding: utf-8 -*-

"""新建分类，编辑分类，删除分类"""
fenlei = {
#                    新建
'点击个人中心':['/html/body/div[1]/div[2]/div[4]/div[2]'],                                    '点击新建分类':['/html/body/div[8]/div[1]/div[2]/div[2]/span[2]'],
'输入分类名称':['/html/body/div[8]/div[1]/div[5]/div/input'],                                 '点击确认':['/html/body/div[8]/div[1]/div[5]/div/div/span[2]'],
'弹窗确认':['/html/body/div[21]/div[7]/div/button'],                                          '文本定位断言':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[1]'],
'数据大屏':['/html/body/div[1]/div[2]/div[3]/span[1]/span'],

#                   编辑
'点击编辑分类':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[4]/span[2]'],    '清除文本框文本信息':['/html/body/div[8]/div[1]/div[5]/div/input'],
'输入汉字':['/html/body/div[8]/div[1]/div[5]/div/input'],                                     '编辑成功弹窗确认':['/html/body/div[21]/div[7]/div/button'],
'输入英文':['/html/body/div[8]/div[1]/div[5]/div/input'],                                      '输入数字':['/html/body/div[8]/div[1]/div[5]/div/input'],
'输入特殊符号':['/html/body/div[8]/div[1]/div[5]/div/input'],                                  '点击编辑确认':['/html/body/div[8]/div[1]/div[5]/div/div/span[2]'],
'分类编辑成功':['/html/body/div[21]/p'],                                                       '分类名称不能重复':['/html/body/div[16]/p'],
'方案名称不得超过十个汉字':['/html/body/div[16]/p'],                                            '分类删除超过':['/html/body/div[16]/p'],

#                    删除
'删除分类':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[4]/span[3]'],           '获取文本定位':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[4]/span[1]'],
'确认删除':['/html/body/div[8]/div[1]/div[6]/div/div/span[2]'],
}

"""方案的数据
                创建，  删除，  编辑                                                               """
plan_data = {
'查看方案':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[1]/span[4]/span[1]'],              '添加方案':['/html/body/div[10]/div/div[2]/div/span'],
'方案名称':["programme_name"],                                                                      '方案分类':['//*[@id="group_id_select"]'],
'主体词':["word01"],                                                                                '分类二':['/html/body/div[10]/div/div[3]/div[1]/p[2]/select/option[2]'],
'地域词库':['/html/body/div[10]/div/div[3]/div[1]/p[4]/span[2]'],                                   '分类方案数':['/html/body/div[8]/div[1]/div[2]/div[3]/div[2]/ul/li[2]/span[2]'],
'河北省下拉框':['//*[@id="tree_37_switch"]'],
'山西省下拉框':['tree_240_switch'],                                                                 '河北省复选框':['//*[@id="tree_37_check"]'],
'唐山市复选框':['//*[@id="tree_63_check"]'],                                                        '地域词不能超过100个汉字':['/html/body/div[16]/p'],
'石家庄市下拉框':['//*[@id="tree_38_switch"]'],                                                      '长安区复选框':['//*[@id="tree_39_check"]'],
'地域词确认':['/html/body/div[10]/div/div[5]/div/div[2]/span[2]'],                                   '事件词':['word02'],
'排除词':['exclude_word'],                                                                          '保存':['/html/body/div[10]/div/div[3]/div[1]/p[7]/span[2]'],
'创建完成 ':['/html/body/div[16]/p'],                                                               '创建完成—确认':['/html/body/div[16]/div[7]/div/button'],
'编辑方案':['/html/body/div[10]/div/div[2]/div/div/div/span[1]'],                                   '删除方案':['/html/body/div[10]/div/div[2]/div/div/div/span[2]'],
'确认删除方案':['/html/body/div[10]/div/div[4]/div/div/span[2]'],                                   '上限弹窗确认':['/html/body/div[16]/div[7]/div/button'],
'方案已达上限':['/html/body/div[16]/p'],                                                            '方案名重复':['/html/body/div[16]/p'],
'请输入方案名称':['/html/body/div[16]/p'],                                                          '请输入主体词':['/html/body/div[16]/p'],
'方案内的词组数不得超过5个':['/html/body/div[16]/p'],                                                 '删除词组1':['/html/body/div[10]/div/div[3]/div[2]/div/span[1]/span[2]'],
'方案名称不得超过20个汉字':['/html/body/div[16]/p'],                                                  '删除词组2':['/html/body/div[10]/div/div[3]/div[2]/div/span[2]/span[2]'],
'删除词组3':['/html/body/div[10]/div/div[3]/div[2]/div/span[3]/span[2]'],                           '删除词组4':['/html/body/div[10]/div/div[3]/div[2]/div/span[4]/span[2]'],
'删除词组5':['/html/body/div[10]/div/div[3]/div[2]/div/span[5]/span[2]'],






}