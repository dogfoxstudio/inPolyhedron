#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
random.seed(time.time())

import inpolyhedron
for i in range(20):
    print(inpolyhedron.test(random.randint(0,6), random.randint(0,6), random.randint(0,6)))
