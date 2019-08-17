settings {
        nodaemon = true
}

sync {
        default.rsyncssh, 
        source="./",
        host="joe",
        targetdir="./server",
        delay = 1,
        rsync = {
            cvs_exclude = true
        }
    }
