settings {
	nodaemon = true
}

sync {
	default.rsyncssh,
	source = ".",
	host = "pi@joe.local",
	targetdir = "server",
	delay = 1,
	excludeFrom = "deploy/.lsyncd-ignore";
	rsync = {
		cvs_exclude = true,
--		binary = "/usr/local/bin/rsync",
		_extra = "--filter=':- .gitignore'"
	},
	ssh = {
--		binary = "/usr/local/bin/ssh",
--		identityFile = "/path/to/.ssh/id_rsa"
	}
}
