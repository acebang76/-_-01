# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:16:39 2021

@author: chban
@name : mini project no. 1
@description : 프로젝트 진행 시 작성되는 소프트웨어 산출물 가이드를 기준을 규칙으로 정해봄.
"""

from durable.lang import *

with ruleset('sw_proc_output'):

    #프로젝트계획(0100)-프로젝트계획서(0101)
    @when_all((m.subject == '프로젝트계획') & (m.object == '프로젝트계획'))
    def ID0101(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '프로젝트계획서'})
    
    #프로젝트계획(0100)-WBS(0102)
    @when_all((m.subject == '프로젝트계획') & (m.object == '프로젝트계획서'))
    def ID0102(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : 'WBS'})
    
    #프로젝트실행(0200)-아키텍쳐정의(0210)-시스템아키텍쳐정의서(0211)
    @when_all((m.subject == '프로젝트실행') & (m.object == '아키텍쳐정의'))
    def ID0211(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '시스템아키텍쳐정의서'})

    #프로젝트실행(0200)-요구정의(0220)-요구사헝정의서(0221)
    @when_all((m.subject == '프로젝트실행') & (m.object == '요구정의'))
    def ID0221(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '요구정의서'})

    #프로젝트실행(0200)-요구정의(0220)-요구사헝추적표(0222)
    @when_all((m.subject == '프로젝트실행') & (m.object == '요구정의서'))
    def ID0222(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '요구사항추적표'})
    
    #프로젝트실행(0200)-분석(0230)-소프트웨어라이선스이행서약서(0231)
    @when_all((m.subject == '프로젝트실행') & (m.object == '분석'))
    def ID0231(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '서식', 'object' : '소프트웨어라이선스이행서약서'})
    
    #프로젝트실행(0200)-설계(0240)-상세설계서(0240)
    @when_all((m.subject == '프로젝트실행') & (m.object == '설계'))
    def ID0240(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '상세설계서'})    

    #프로젝트실행(0200)-설계(0240)-클래스다이어그램(0241)
    @when_all((m.subject == '프로젝트실행') & (m.object == '상세설계서'))
    def ID0241(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '클래스다이어그램'})    
        
    #프로젝트실행(0200)-설계(0240)-시퀀스다이어그램(0242)
    @when_all((m.type == '문서') & (m.object == '클래스다이어그램'))
    def ID0242(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '시퀀스다이어그램'})  

    #프로젝트실행(0200)-설계(0240)-프로그램목록(0243)
    @when_all((m.type == '문서') & (m.object == '시퀀스다이어그램'))
    def ID0243(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '프로그램목록'})  

    #프로젝트실행(0200)-설계(0240)-시스템인터페이스정의서(0244)
    @when_all((m.type == '문서') & (m.object == '프로그램목록'))
    def ID0244(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '시스템인터페이스정의서'})  

    #프로젝트실행(0200)-설계(0240)-UI정의서(0245)
    @when_all((m.type == '문서') & (m.object == '시스템인터페이스정의서'))
    def ID0245(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : 'UI정의서'})  

    #프로젝트실행(0200)-설계(0240)-물리ERD(0246)
    @when_all((m.type == '문서') & (m.object == 'UI정의서'))
    def ID0246(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '물리ERD'})  

    #프로젝트실행(0200)-설계(0240)-논리ERD(0247)
    @when_all((m.type == '문서') & (m.object == '물리ERD'))
    def ID0247(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '논리ERD'}) 

    #프로젝트실행(0200)-설계(0240)-테이블정의서(0248)
    @when_all((m.type == '문서') & (m.object == '논리ERD'))
    def ID0248(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '테이블정의서'}) 

    #프로젝트실행(0200)-구현(0250)-소스코드(0251)
    @when_all((m.subject == '프로젝트실행') & (m.object == '구현'))
    def ID0251(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '파일', 'object' : '소스코드'}) 

    #프로젝트실행(0200)-구현(0250)-SW라이선스목록(0252)
    @when_all((m.type == '파일') & (m.object == '소스코드'))
    def ID0252(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '서식', 'object' : 'SW라이선스목록'}) 

    #프로젝트실행(0200)-구현(0250)-오픈소스검증결과서(0253)
    @when_all((m.type == '서식') & (m.object == 'SW라이선스목록'))
    def ID0253(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '서식', 'object' : '오픈소스검증결과서'}) 

    #프로젝트실행(0200)-테스트(0260)-테스트계획서(0261)
    @when_all((m.subject == '프로젝트실행') & (m.object == '테스트'))
    def ID0261(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '테스트계획서'}) 

    #프로젝트실행(0200)-테스트(0260)-테스트결과서(0262)
    @when_all((m.type == '문서') & (m.object == '테스트계획서'))
    def ID0262(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '테스트결과서'}) 

    #프로젝트실행(0200)-이행(0270)-사용자매뉴얼(0271)
    @when_all((m.subject == '프로젝트실행') & (m.object == '이행'))
    def ID0271(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '사용자매뉴얼'}) 

    #프로젝트실행(0200)-이행(0270)-운영자매뉴얼(0272)
    @when_all((m.type == '문서') & (m.object == '사용자매뉴얼'))
    def ID0272(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '운영자매뉴얼'}) 

    #프로젝트종료(0300)-완료(0300)-프로젝트완료보고서(0301)
    @when_all((m.subject == '프로젝트종료') & (m.object == '완료'))
    def ID0301(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '프로젝트완료보고서'}) 

    #프로젝트관리(0400)-결함관리(0430)-결함관리대장(0431)
    @when_all((m.subject == '프로젝트관리') & (m.object == '결함관리'))
    def ID0431(c):
        c.assert_fact({'subject' : c.m.subject, 'type' : '문서', 'object' : '결함관리대장'}) 

    @when_all((+m.subject)) # m.subject가 한번 이상
    def output(c):
        print('Fact: {0} 프로세스에는 {1} 형식의 {2} 산출물을 제출해야 한다'.format(c.m.subject, c.m.type, c.m.object))
        
assert_fact('sw_proc_output', {'subject' : '프로젝트계획', 'type' : '문서', 'object' : '프로젝트계획'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '문서', 'object' : '아키텍쳐정의'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '문서', 'object' : '요구정의'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '서식', 'object' : '분석'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '문서', 'object' : '설계'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '서식', 'object' : '구현'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '문서', 'object' : '테스트'})
assert_fact('sw_proc_output', {'subject' : '프로젝트실행', 'type' : '문서', 'object' : '이행'})
assert_fact('sw_proc_output', {'subject' : '프로젝트종료', 'type' : '문서', 'object' : '완료'})
assert_fact('sw_proc_output', {'subject' : '프로젝트관리', 'type' : '문서', 'object' : '결함관리'})

# subject   : 메가프로세스
# type      : 형식
# object    : 단계 -> 필수산출물 (단계를 입력하면 룰셋을 통해 규칙으로 정해진 필수산출물이 단계와 함께 출력된다.)