#!/usr/bin/env python3
# Created By: J.Medlock
# Created On: 2017.10.18
 
import PTN
import os
import logging
import shutil
from titlecase import titlecase
 
log = logging.getLogger("torrent-process")
 
class WorkableFile:
 
    def __init__(self, path=None, fname=None, meta=None):
        # define vars for this class here
        self.path = path # full path of the file
        self.fname = fname # file name only
        self.meta = meta # PTN object with all info from the file.
 
    """Quick helper function that checks for a season and episode number. More than likely will be a TV Episode"""
    def isTV(self):
        if self.meta is None:
            return False
 
        # test a couple things
        if "episode" in self.meta and "season" in self.meta:
            return True
        else:
            return False

    """This function determines if the file is a movie or not"""
    def isMovie(self):
        if self.meta is None:
            return False

        if "year" in self.meta:
            return True
        else:
            return False
 
    def fixTitle(self):
        if self.meta is not None:
            self.meta["title"] = titlecase(self.meta["title"])
 
"""The responsibility of this function is to walk the download directory
and then identify which files we are going to work with. This will return
a list of WorkablFile objects."""
def walk_downloads(dpath):
    target_exts = ('.avi', '.mkv', '.mp4', '.mpg', '.srt')
    records = list()
 
    if not isinstance(dpath, str):
        log.error("Internal: walk_downloads recieves something other than a string for the path")
        raise TypeError("walk_downloads recieves something other than a string for the path")
 
    # Walk everything
    for root, dirs, files in os.walk(dpath):
        for name in files:
            if name.endswith(target_exts):
                records.append(WorkableFile(os.path.join(root, name), name))
 
    return records
 
def parse_meta(workablefiles):
 
    if not isinstance(workablefiles, list):
        log.error("Internal: parse_meta was passed something that isn't a list")
        raise TypeError("Internal: parse_meta was passed something that isn't a list")
 
    for record in workablefiles:
        if not isinstance(record, WorkableFile):
            log.warning("Unknown object in workablefiles list")
            continue
 
        if record.fname is None:
            log.warning("Record does not have a file name, skipping")
            continue
 
        record.meta = PTN.parse(record.fname)
        record.fixTitle()
 
def format_epi_file(title, season, episode, container):
    #My way
    #return "{0}.S{1}.E{2}.{3}".format(title.replace(" ", "."), season, episode, container)
    #Your way
    return "{0} - S{1}E{2}.{3}".format(title, "%02d" % season, "%02d" % episode, container)

# Formats the movie name to "Title - (year).container
def format_movie_name(title, year, container):
    return "{0} - ({1}).{2}".format(title, "%04d" % year, container)
 
def process_move(workableFiles, basepath, copy=False):
 
    newDirectory = None
    newFullPath = None
 
    for record in workableFiles:
        if record.isTV():
            newDirectory = os.path.join(basepath, "TV",
                                        str(record.meta["title"]),
                                        "Season {0}".format(record.meta["season"]))
            newFullPath = os.path.join(newDirectory, format_epi_file(record.meta["title"],
                                                                  record.meta["season"],
                                                                  record.meta["episode"],
                                                                  record.meta["container"]))
        elif record.isMovie():
            newDirectory = os.path.join(basepath, "Movies")
                                        #str(record.meta["title"]),
                                        #"Year {0}".format(record.meta["year"]))
            newFullPath = os.path.join(newDirectory, format_movie_name(record.meta["title"],
                                                                    record.meta["year"],
                                                                    record.meta["container"]))
# check if the new directory exists
            if not os.path.exists(newDirectory):
                os.makedirs(newDirectory)

                if copy:
                    # Copy it!
                    shutil.copy(record.path, newFullPath)
                    # Move it!
                    shutil.move(record.path, newFullPath)

if __name__ == '__main__':
    done_var = True
    paths = {
        "torrent_root": "/home/<username>/Torrents",
        #"videos_root":"/home/<username>/Videos/Completed"
        "shows_complete": "/home/<username>/Videos",
        "movies_complete": "/home/<username>/Videos/movies"
    }
 
    workables = list() #List of WorkableFile objects
 
   # check our paths
    """for key, val in iter(paths):
        if not os.path.exists(val):
            errorstr = str("The {0} directory does not exist or cannot be accessed: {1}".format(key, val))
            raise NotADirectoryError(errorstr)"""
 
    # get to work
    #workables = walk_downloads(paths["torrent_root"])
    #parse_meta(workables)
    #process_move(workables, paths["shows_complete"], True)

    if done_var is True:
        if True:
            workables = walk_downloads(paths["torrent_root"])
            parse_meta(workables)
            process_move(workables, paths["shows_complete"], True)
        else:
            log.warning("Unable to properly parse information")
    else:
        log.error("There was an error ")
