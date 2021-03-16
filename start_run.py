#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: start_run.py
# @time: 2020/11/8 5:23 下午

from httprunner.api import HttpRunner
runner = HttpRunner()
runner.run( 'testcases/20201101/demo_01.yml' )