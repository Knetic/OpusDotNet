#!/usr/bin/env python

# Invokes a build of this project's assets as a unitypackage.

import sys
import os
import subprocess
from distutils.spawn import find_executable

# Determines a Unity editor executable that is available from the PATH.
# If none can be found, returns None.
def determineUnityExecutable():

	possibleExecutables = ["Unity", "unityEditor"]

	for executable in possibleExecutables:

		actualExecutable = find_executable(executable)
		if(actualExecutable != None):
			return actualExecutable
	return None

def main():

	workingDirectory = os.getcwd()
	baseDirectory = os.path.basename(os.path.normpath(workingDirectory))
	executable = determineUnityExecutable()

	if(executable == None):
		print("Unable to find unity executable, make sure either 'Unity' or 'unityEditor' are available within your path.")
		sys.exit(1)

	# Shellout.
	arguments = [
		executable,
		"-batchmode",
		"-nographics",
		"-quit",
		"-projectPath",
		workingDirectory,
		"-exportPackage",
		"Assets",
		baseDirectory + ".unityPackage"
	]
	
	friendlyArguments = ' '.join(arguments)
	print("Calling Unity: [" + friendlyArguments + "]")

	statusCode = subprocess.call(arguments, shell=False, stdout=sys.stdout, stderr=sys.stderr)
	if(statusCode != 0):
		print("Call to unity failed with status code " + str(statusCode))

	return statusCode

sys.exit(main())
