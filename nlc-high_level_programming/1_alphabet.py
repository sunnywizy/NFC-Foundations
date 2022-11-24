#!/usr/bin/python3
"""Printing alphabet for a-z except q and e using ASCII alphabet"""
for i in range(97,123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end = " ")