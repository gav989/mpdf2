#!/usr/bin/env python3
import subprocess, os
for i in range(1,101):
	subprocess.call(["python", "quadraticfactorisation1.py"])
	subprocess.call(["rename", "1", str(i), "QuadraticFactorisation1.pdf"])