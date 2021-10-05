install-composer:
	@echo "Installing Composer based on https://getcomposer.org/download/"
	@php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
	@php composer-setup.php
	@php -r "unlink('composer-setup.php');"

install:
	@echo "Installing dependencies"
	@./composer.phar install

remove-composer:
	@rm composer.phar

clean:
	@rm composer.lock
	@rm -rf vendor

run:
	php SigVerifyPhp.php

help:
	@echo "To download composer, execute:"
	@echo "   make install-composer"
	@echo "To download dependencies, execute:"
	@echo "   make install"
	@echo "To remove composer:"
	@echo "   make remove-composer"
	@echo "To clean dependencies, execute:"
	@echo "   make clean"
	@echo "To run, execute:"
	@echo "   make run"
