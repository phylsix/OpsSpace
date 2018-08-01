#---------------------------------------------------------------------------------------------------
# This is the site where the script is run at. The only thing this affects is the LFN
# to PFN translation of the unmerged directory, which can be overwritten directly using **UNMERGED_DIR_LOCATION**.

SITE_NAME = 'DUMMYNAME'

#---------------------------------------------------------------------------------------------------
# The Unmerged Cleaner tool cleans the directory matching this LFN. On most sites, this
# will not need to be changed, but it is possible for a /store/dcachetests/unmerged
# directory to exist, for example. The default is '/store/unmerged'.

LFN_TO_CLEAN = '/store/unmerged'

#---------------------------------------------------------------------------------------------------
# The location, or PFN, of the unmerged directory. This can be
# retrieved from Phedex (default) or given explicitly.

UNMERGED_DIR_LOCATION = LFN_TO_CLEAN

#---------------------------------------------------------------------------------------------------
# Determines whether a list of directories or files will be generated.
# These lists will be in PFN format. Possible values are
# 'directories' or 'files'. The default is 'directories'.

WHICH_LIST = 'directories'

#---------------------------------------------------------------------------------------------------
# The list of directory or file PFNs to delete are placed this file.
# The default is '/tmp/<WHICH_LIST>_to_delete.txt'.

DELETION_FILE = '/tmp/%s_to_delete.txt' % WHICH_LIST

#---------------------------------------------------------------------------------------------------
# This is the number of seconds between each deletion of a directory or file.
# The sleep avoids overloading the system and allows the operator to interrupt a deletion.
# The default is 0.5.

SLEEP_TIME = 0.5

#---------------------------------------------------------------------------------------------------
# The directories in this list are left alone. Only the top level of directories within
# the unmerged location is checked against this if WHICH_LIST is 'directories'.
# The defaults are ['SAM', 'logs'].

DIRS_TO_AVOID = ['SAM', 'logs']

#---------------------------------------------------------------------------------------------------
# Directories with an age less than this, in seconds, will not be deleted.
# 1209600 corresponds to two weeks.
# Mathematical expressions here are evaluated.

MIN_AGE = 1209600 * 2

#---------------------------------------------------------------------------------------------------
# This defines the storage type of the site. This may be necessary for the script to run
# correctly or optimally. Acceptable values are 'posix' and 'hadoop'.
# The default is 'posix'.

STORAGE_TYPE = 'posix'
