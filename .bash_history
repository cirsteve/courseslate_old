ls
mkdir .ssh
mv id_rsa.pub .ssh/authorized_keys
chown -R steve:steve .ssh
chmod 700 .ssh
chmod 600 .ssh/authorized_keys 
sudo vim /etc/ssh/sshd_config 
sudo /etc/init.d/ssh reloa
sudo /etc/init.d/ssh reload
exit
sudo /etc/init.d/postgresql-8.4 restart
cd
cd sites/rdw/app/
ls
vim settings.py
python manage.py syncdb
vim settings.py
python manage.py syncdb
sudo /etc/init.d/apache2 restart
cd /etc/apache2/
ls
cd sites-available/
ls
sudo vim ropeadopeandwink.com 
sudo /etc/init.d/apache2 restart
sudo vim ropeadopeandwink.com 
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/apache2 restart
a2ensite ropeadopeandwink.com
cd
cd sites/rdw/app/
ls
cat django.wsgi
ls
vim django.wsgi 
cat django.wsgi 
sudo /etc/init.d/apache2 restart
vim django.wsgi 
sudo /etc/init.d/apache2 restart
sudo vim /etc/apache2/sites-available/ropeadopeandwink.com 
mkdir ../application
ls
cp -r * ../application/
sudo /etc/init.d/apache2 restart
cd ..
ls
cd application/
ls
sudo vim settings.py
cd /etc/apache2/
ls
cat httpd.conf 
cat apache2.conf 
ls
cat httpd.conf
cd
cd sites/rdw/application/
ls
vim django.wsgi 
sudo /etc/init.d/apache2 restart
cd /etc/apache2/
ls
ls sites-enabled/
cd sites-available/
sudo vim ropeadopeandwink.com 
sudo /etc/init.d/apache2 restart
cd
cd sites/rdw/
ls
rm -r app
cd application/
ls
vim settings.py
sudo /etc/init.d/apache2 restart
vim settings.py
sudo /etc/init.d/apache2 restart
ls
ls 
ls templates/
vim settings.py
sudo /etc/init.d/apache2 restart
vim settings.py
sudo /etc/init.d/apache2 restart
vim settings.py
ls
cd templates/
ls
vim base.html
sudo /etc/init.d/apache2 restart
cd //
cd
cd sites/rdw/application/
ls
vim settings.py
cd templates/
vim base.html
cd ..
vim settings.py
sudo /etc/init.d/apache2 restart
vim settings.py
sudo /etc/init.d/apache2 restart
vim settings.py
sudo /etc/init.d/apache2 restart
vim templates/base.html
sudo /etc/init.d/apache2 restart
cd ..
ls
ls static/
ls static/css
cd application/
vim settings.py
sudo /etc/init.d/apache2 restart
ls
cd media/
ls
cd ..
ls static/
cd ..
ls
ls static/
ls media/
cat application/settings.py
ls
cp -r admin static/
ls
ls static
;s
vim application/settings.py
sudo /etc/init.d/apache2 restart
cd application/
vim settings.py
sudo /etc/init.d/apache2 restart
ls
python manage.py loaddata entry.json
ls
vim settings.py
ls
cd ..
ls
cd static/
ls
mkdir admin
ls
cp -r admin css
sudo /etc/init.d/apache2 restart
cd ..
ls
cd static
ls
cd css
ls
cd ..
cd ../application/
vim settings.py
sudo /etc/init.d/apache2 restart
cd
ls
cd textile-2.1.5
ls
sudo python setup.py install
cd 
cd sites/rdw/application/
sudo /etc/init.d/apache2 restart
ls
vim settings.py
sudo pip install Markdown
vim settings.py
sudo /etc/init.d/apache2 restart
vim templates/bio.html
exit
su -u postgres creatuser -P rdwadmin
sudo -u postgres creatuser -P rdwadmin
su postgres
exit
sudo vim /etc/postgresql/8.4/main/pg_hba.conf 
sudo /etc/init.d/postgresql-8.4 restart
cd 
cd sites/rdw/app/
ls
python manage.py syncdb
sudo vim /etc/postgresql/8.4/main/pg_hba.conf 
sudo /etc/init.d/postgresql-8.4 restart
cd
cd sites/rdw/app/
ls
python manage.py syncdb
su postgres
quit
exit
cd
cd sites/rdw/app/
ls
vim settings.py
python manage.py syncdb
cd /etc/postgresql
ls
cd 8.4/
ls
cd main/
ls
sudo vim pg_hba.conf 
sudo /etc/init.d/postgresql-8.4 restart
cd
cd sites/rdw/app/
python manage.py syncdb
cd /etc/postgresql/
ls
cd 8.4/main/
sudo vim pg_hba.conf 
sudo /etc/init.d/postgresql-8.4 restart
cd 
cd sites/rdw/app/
sudo python manage.py syncdbn
sudo python manage.py syncdb
ls
vim settings.py
sudo python manage.py syncdb
vim setting.py
vim settings.py
cd
ls
cd /etc/postgresql/8.4/main/
ls
sudo vim pg_hba.conf 
sudo /etc/init.d/postgresql-8.4 restart
cd
cd sites/rdw/ap
cd sites/rdw/app/
ls
sudo python manage.py syncdb
su postgres
sudo vim /etc/ssh/sshd_config 
apt-get install python-setuptools lib-apache2-mod-wsgi
sudo apt-get install python-setuptools lib-apache2-mod-wsgi
sudo apt-get install python-setuptools libapache2-mod-wsgi
sudo apt-get install postgresql python-psycopg2
sudo apt-get install nginx
apt-get install memcached
sudo apt-get install memcached
cd
sudo apt-get install git
sudo apt-get install svn
apt-get install git-core gitosis
sudo apt-get install git-core gitosis
sudo apt-get install subversion
svn co http://code.djangoproject.com/svn/django/trunk/
python
ls
cd trunk
ls
cat LICENSE 
ls
cat INSTALL 
sudo python setup.py install
python
cd /usr/local/lib/python2.6/dist-packages/
ls
rm -r django
sudo rm -rf django
ls
sudo rm Django-1.4_pre_alpha.egg-info 
cd
wget http://www.djangoproject.com/download/1.3/tarball/
ls
cd trunk
ls
sudo python setup.py install
ls
python
ls
cd /usr/local/lib/python2.6/
ls
cd dist-packages/
ls
cd django/
ls
cd ..
sudo rm -rf *
ls
cd /usr/lib/python2.6/
ls
cd dist-packages/
ls
cd
ls
sudo rm -rf trunk
python
wget http://www.djangoproject.com/download/1.3/tarball/
ls
ls -l
cat index.html
62;9;c62;9;c62;9;c62;9;c62;9;c
ls
wget http://www.djangoproject.com/download/1.3/tarball/Django-1.3.tar.gz
http://www.djangoproject.com/download/1.3/tarball/cd
ls
tar -zxvf Django-1.3.tar.gz 
ls
rm -rf Django-1.3
tar -zxvf Django-1.3.tar.gz 
ls
cd Django-1.3
ls
sudo python setup.py install
python
cd
ls
mkdir sites
cd sites
ls
mkdir rdw
cd rdw
ls
git init
git remote add origin git@github.com:cirsteve/ropeadopeandwink.git
git pull origin master
ls
cd ../..
ls
mkdir rdw
postgres
pgre
pg
psql -s mydb
sudo passwd postgres
su postgres
adduser dbadmin
sudo adduser dbadmin
python manage.py syncdb
ls 
vim settings.py
cd /etc
ls
cd postgresql
ls
cd 8.4/
ls
cd main/
ls
ls -l
cat pg_ident.conf 
sudo cat pg_ident.conf 
sudo vim pg_ident.conf 
ls
sudo cat pg_hba.conf 
su postgres
ls
cd rdw
ls
vimm settings.py
vim settings.py
cat settings.py
ls
cd ..
ls
ls sites/
ls sites/rdw
rmdir sites/rdw
cd sites/
ls
rm -rf rdw
cd ..
ls
cp -r rdw sites
ls sites
ls sites/rdw/
cd sites/rdw
ls
rm local*
touch django.wsgi
vim django.wsgi
mkdir app
ls
rmdir app
mkdir ../app
pwd
mkdir app
ls
ls ..
rmdir app
ls
cp -rf * ../app
ls
cd ..
ls
ls app
ls
cd rdw
ls
rm -rf *
ls
cd ..
ls
cd app
ls
cp media ..
cd ..
ls
cd rdw
ls
cd ..
ls
cd ..
ls
cd rdw
ls
cp -r media ../sites/rdw/
cd /usr/local/lib/python2.6/dist-packages/django/
ls
cd contrib/
ls
cp -r admin /home/steve/sites/rdw
cd
cd sites/rdw/
ls
cd ..
cd rdw
ls
cd ..
ls
ls app
ls
mv -rf app rdw
mv -R app rdw
cp -r app rdw
ls rdqw
ls rdw
cd rdw
cd apps
cd app
ls
cp -r static ..
ls
vim settings.py
cd /etc/apache2
ls
ls -l
cat apache2.conf 
ls
cat httpd.conf 
ls
cd sites-available/
ls
touch ropeadopeandwink.com
sudo touch ropeadopeandwink.com
ls
vim ropeadopeandwink.com 
ls
ls -l
sudo vim ropeadopeandwink.com 
sudo a2ensite ropeadopeandwink.com
cd
cd sites
ls
cd rdw
ls
mkdir logs
ls
cd app
python manage.py syncdb
sudo pip install textile-2.1.5
sudo easy_install pip
sudo pip install textile-2.1.5
cd
wget http://pypi.python.org/packages/source/t/textile/textile-2.1.5.tar.gz#md5=6e030e112eca1dafa1be84cf5575560d
ls 
tar -zxvf text
tar -zxvf textile-2.1.5.tar.gz 
ls
cd textile-2.1.5
ls
sudo python setup/py install
sudo python setup.py install
cd
ls
mkdir repos
cd repos
git clone https://github.com/cirsteve/django-tagging.git
ls
cd django-tagging/
ls
sudo python setup.py install
cd
ls
cd sites/rdw/
cd app/
python manage.py syncdb
cd
ls
wget http://pypi.python.org/packages/source/d/django-treebeard/django-treebeard-1.61.tar.gz#md5=eecc036cde8d4b899cea4dc4da86441e
ls
tar -zxvf django-treebeard-1.61.tar.gz 
ls
cd django-treebeard-1.61
ls
sudo python setup.py install
cd
cd sites/rdw/a
cd sites/rdw/app/
ls
python manage.py syncdb
sudo apt-get install python-dev
sudo apt-get install PIL
sudo apt-get install libjpeg-dev libjpeg62 libjpeg62-dev zlib1g-dev libfreetype6 libfreetype6-dev
cd
sudo pip install PIL
cd sites/rdw/app/
python manage.p syncdb
python manage.py syncdb
ls
vim settings.py
python manage.py syncdb
su dbadmin
adduser dbadmin
sudo adduser dbadmin
su - postgrea
su - postgres
ls
mkdir gsites
ls sites/
ls
cd gsites/
ls
mkdir app
ls ../sites
ls ../sites/rdw
mkdir rdw
cd ../sites/rdw
ls
cp -r * ../../gsites/rdw/
cd ../../gsites/rdw/
ls
cd application/
ls

cd ..
rm -rf application/
mkdir application
cs application/
git init
ls -a
rm -rf .git
ls
cd application/
ls
git init
ls -a
pwd
ls
rm -rf .git
ls
ls -a
git init git@github.com:cirsteve/ropeadopeandwink.git
ls
ls -l
ls
rm -rf git\@github.com\:cirsteve/
ls
git clone git@github.com:cirsteve/ropeadopeandwink.git
ls
sudo git clone git@github.com:cirsteve/ropeadopeandwink.git
exit
cd sites
ls
cd ..
cd gsites/
ls
cd rdw
ls
cd application/
git clone https://github.com/cirsteve/ropeadopeandwink.git
ls
cd ropeadopeandwink/
ls
pwd
ls
ls -a
pwd
ls
ls -a
git pull origin
cd /etc/apache2/
ls
cat sites-available/ropeadopeandwink.com 
cat /hosts
cat hosts
cat hostname
ls
cat httpd.conf 
cat envvars 
exit
ls
wget http://media.djangoproject.com/releases/1.3/Django-1.3.1.tar.gz
ls
tar -zxvf Django-1.3.1.tar.gz 
ls
cd /usr/local/lib/python2.6/dist-packages/
ls
sudo rm-rf django
sudo rm -rf django
ls
rm Django-1.3.egg-info 
sudo rm Django-1.3.egg-info 
cd
ls
cd Django-1.3.1
ls
sudo python setup.py install
sudo apt-get update
sudo apt-get upgrade
ls
pwd
cd .ssh
ls
cd
ssh -T git@github.com
ls .ssh
ls
cd
ls
ls rdw
ls -a rdw
pwd
ls
cd rdw
ls
cat templates/entry/entry_detail.html
cat templates/base.html
cd ..
ls
cd sites/
ls
cd app/
ls
cd ..
cd rdw/
ls
cd application/
ls
cd ..
ls
ls static/
cd application/
cat django.wsgi 
cat /etc/apache2/sites-available/ropeadopeandwink.com 
cd
ls
cd rdw
ls
rm local*
ls
cat settings.py
ls
vim settings.py
ls static/
ls static/rdw/
cd static/
ls
rm -rf css
ls
cd ..
ls
cd ..
ls
cd sites/
ls
cd rdw/
ls
cd application/
cat settings.py
cd
ls
cd rdw
ls
vim settings.py
cd
cd sites/
ls
cd rdw/
ls
cd static/
ls
cp r admin /home/steve/rdw/static/rdw/
cp -r admin /home/steve/rdw/static/rdw/
cd
cd rdw/
ls
cp rf * ../sites/rdw/application/
cp -rf * ../sites/rdw/application/
cd static/
ls
cd rdw/
ls
cd ..
ls
cp -rf rdw ../../sites/rdw/static/
cd ../../sites/rdw/application/
ls
sudo /etc/init.d/apache2 reload
vim settings.py
sudo /etc/init.d/apache2 reload
vim settings.py
sudo /etc/init.d/apache2 reload
ls
cd templates/
cat base.html
vim entry/entry_detail.html
cd ..
cat settings.py
cd ..
cd static/
ls
ls rdw
ls
rm -rf admin
rm -rf css
ls
cd ../application/
cat settings.py
python manage.py staticcollect
python manage.py collectstatic
cd
ls /usr/local/lib/python2.6/dist-packages/
cd
ls
cd sites/
ls
mkdir cs
cd cs
mkdir logs
mkdir application
mkdir media
mkdir static
cd
ls
cd courseslate_d/
;s
ls
rm local*
rm db.db
ls
cp -r * ../sites/cs/application/
cd ../sites/cs/application/
ls
cp build/django.wsgi .
ls
python manage.py syncdb
cd
ls
hg clone https://bitbucket.org/ubernostrum/django-registration
apt-get install hg
sudo apt-get install hq
sudo apt-get install hg
sudo apt-get install mercurial
hg clone https://bitbucket.org/ubernostrum/django-registration
ls
cd django-
cd django-registration/
ls
sudo python setup.py install
cd
cd sites/cs/application/
python manage.py syncdb
python manage.py loaddata ar.json
python manage.py loaddata mys.json
cd build
ls
cp apache/courseslate.com /etc/apache2/sites-available/
sudo cp apache/courseslate.com /etc/apache2/sites-available/
sudo a2ensite courseslate.com
cd ../nginx
sudo cp nginx/courseslate.com /etc/nginx/sites-available/
cd /etc/nginx
ls
ls sites-available/
ln -s sites-available//courseslate.com sites-enabled/
sudo ln -s sites-available//courseslate.com sites-enabled/
cd
cd sites/cs/application/
python manage.py collectstatic
vim settings.py
python manage.py collectstatic
vim settings.py
python manage.py collectstatic
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/nginx reload
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/nginx restart
cd /etc/apache2
ls
sudo vim ports.conf 
sudo /etc/init.d/apache2 reload
sudo vim ports.conf 
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/nginx restart
cd ../nginx
ls
cat nginx.conf 
ls sites-enabled/
cd sites-enabled/
ls -l
sudo rm courseslate.com
ls
sudo ln -s ../sites-available/courseslate.com 
ls
sudo /etc/init.d/nginx restart
sudo /etc/init.d/apache2 reload
cd ..
ls
cat sites-available/courseslate.com 
ls
ls conf.d/
cat nginx.conf 
cd
cd sites/cs/
ls
cd logs/
ls
cd lo
cd logs
cat error.log 
cd ../application/
ls
cat django.wsgi 
cd
cd sites/cs/application/
cat settings.py
ls
ls -l
ls
ls ../../rdw/application/
cat ../../rdw/application/django.wsgi 
cat django.wsgi 
vim settings.py
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/nginx reload
sudo /etc/init.d/apache2 reload
ls
cd ..
ls
cd logs
ls
cat access.log
cat error.logs
cat error.log
cat ../application/urls.py
cd ../application/
python manage.py shell
cat ../logs/error.log 
vim mystudy/views.py
vim mystudy/forms.py
cat ../logs/error.log 
vim settings.py
sudo /etc/init.d/apache2 reload
vim settings.py
ls
vim mystudy/forms.py
sudo /etc/init.d/apache restart
sudo /etc/init.d/apache2 restart
cd
ls
rm -rf courseslate_d/
ls
cd courseslate_d/
ls
rm local*
rm db.db
ls
ls ../sites/cs/application/
cp -rf * ../sites/cs/application/
cat ../sites/cs/application/settings.py
cd ..
ls
cd crs
ls
cp -rf * ../sites/cs/application/
cd ../sites/cs/application/
ls
rm local*
rm db.db
ls
sudo /etc/init.d/apache2 reload
vim mystudy/forms.py
sudo /etc/init.d/nginx restart
sudo /etc/init.d/apache2 reload
vim mystudy/models.py
sudo /etc/init.d/apache2 reload
vim urls.py
sudo /etc/init.d/apache2 reload
ls
ls ../static/
mkdir ../static/cs
vim settings.py
ls
ls static/
python manage.py collectstatic
sudo /etc/init.d/nginx reload
cd ../static
ls
ls admin/
cat /etc/nginx/sites-available/courseslate.com 
ls
ls cs
rmdir cs
cd /usr/local/lib/python2.6/dist-packages/
ls
cd django
ls
cd contrib/
ls
cd admin
ls
ls media/
cp -r media /home/steve/sites/cs/static/admin
sudo /etc/init.d/apache2 reload
cd ~/sites/cs
ls
ls static
ls admin
ls static/admin/
sudo /etc/init.d/nginx restart
ls
vim application/settings.py
sudo /etc/init.d/apache2 reload
cd application/templates/
touch 404.html
vim 404.html 
cd registration/
ls
vim activation_email.txt
vim activation_email_subject.txt
cd ..
vim base.html
cd ..
vim settings.py
sudo /etc/init.d/apache2 reload
cat settings.py
vim settings.py
sudo /etc/init.d/apache2 reload
vim settings.py
sudo /etc/init.d/apache2 reload
vim settings.py
sudo /etc/init.d/apache2 reload
cd /etc/nginx
cat sites-available/ropeadopeandwink.com 
cat sites-available/courseslate.com 
cd
vim sites/rdw/application/settings.py
sudo /etc/init.d/apache2 reload
ls
ls sites/
rm -rf rdw
ls
cd sites/
ls
ls rdw
ls rdw/static
cd /etc/
cd nginx
ls
less nginx.conf
cat nginx.conf
ls
ls conf.d/
cd sites-enabled/
ls
touch ropeadopeandwink.com
sudo touch ropeadopeandwink.com
ls
sudo vim ropeadopeandwink.com 
cd ../..
cd apache2/
ls
ls sites-available/
ls sites-enabled/
cd sites-available/
ls
sudo vim ropeadopeandwink.com 
sudo /etc/init.d/apache2 reload
sudo /etc/init.d/nginx reestart
sudo /etc/init.d/nginx restart
cd ../../nginx/
ls
cat nginx.conf
ls 
cd sites-enabled/
ls
mv ropeadopeandwink.com ../sites-available/
sudo mv ropeadopeandwink.com ../sites-available/
ls
ln -s ../sites-available/ropeadopeandwink.com 
sudo ln -s ../sites-available/ropeadopeandwink.com 
ls
sudo /etc/init.d/nginx restart
cd
cd sites/rdw
ls
cd /etc/nginx/sites-available/
sudo vim ropeadopeandwink.com 
sudo /etc/init.d/nginx restart
sudo  /etc/init.d/apache2 stop
sudo /etc/init.d/nginx restart
sudo /etc/init.d/apache2 start
cd ../../apache2/
ls
cat sites-available/ropeadopeandwink.com 
ls
sudo vim ports.conf 
sudo /etc/init.d/apache2 start
cd ../nginx
ls
cat mime.types 
cat nginx.conf 
ls /home/steve/sites/rdw
sudo /etc/init.d/nginx reload
sudo vim sites-available/ropeadopeandwink.com 
sudo /etc/init.d/nginx reload
su postgres
cd sites/cs/application/
ls
cat templates/mystudy/updates_list.html
vim sites/cs/application/templates/base.html
cd sites/
pwd
ls
cd cs
ls
ls static
ls
cd static
ls
ls admin/
ls admin/media
cat ../application/settings.py
vim ../application/settings.py
sudo /etc/init.d/apache2 reload
ssh-agent
exit
ssh -T git@github.com
exit
ssh -T git@github.com
ls .ssh
exit
ssh -T git@github.com
exit
ssh -T git@github.com
ssh -T git@github.com
ssh -T git@github.com
ssh-agent restart
ssh-agent
ssh-agent restart 2160
ssh -T git@github.com
vim sites/rdw/application/templates/bio.html
cat /etc/nginx/sites-available/ropeadopeandwink.com 
cat /etc/nginx/sites-available/courseslate.com 
sudo vim /etc/nginx/sites-available/courseslate.com 
sudo vim /etc/nginx/sites-available/ropeadopeandwink.com 
sudo /etc/init.d/nginx reload
vim sites/rdw/application/templates/bio.html
cd /etc/nginx
ls
cat nginx.conf
ls
ls conf.d/
sudo touch proxy.conf
ls
sudo vim proxy.conf 
sudo vim sites-available/ropeadopeandwink.com 
sudo /etc/init.d/nginx restart
ls
cd courseslate_d/
ls
rm local*
cat settings.py
ls
cat urls.py
cp -r ../sites/cs/ ../csb
cp -rf * ../sites/cs/application/
cd ../sites/cs/application/
ls
cat django.wsgi 
cat settings.py
cat ~/csb/application/settings.py
sudo /etc/init.d/apache2 reloiad
sudo /etc/init.d/apache2 reload
vim urls.py
sudo /etc/init.d/apache2 reload
vim templates/includes/pr_list_inc.html
vim templates/includes/tr_list_inc.html
vim  sites/cs/application/tagging/fields.py
exit
cd sites/cs/application/
ls
rm -rf csg.git
cd ../..
cd ..
ls
ls gsites
mkdir gsites/cs
cd gsites/
mkdir cs/application && mkdir cs/static
ls
ls cs
cd cs
mkdir logs
mkdir media
ls
cd application/
ls
ls -a
git init
ls
rm -r .
rm -r *
ls
tar -zxvf csg.git.tgz 
ls
ls csg.git
ls
mkdir .git
ls
ls -a
rm -rf .git
mkdir .git
cd csg.git
ls
cp -r * ../.git
cd ..
ls
ls -a
ls
mkdir .git
ls -a
ls .git
ls -a
mv csg.git ~
ls
rm .gitignore
ls -a
mv csg.git.tgz ~
ls
ls -a
pwd
ls -a
cd
ls
cp csg.git gsites/
ls
ls gsites/
cp -r csg.git gsites/
ls gsites/
cd sites/rdw/application/templates/
vim base.html
cd sites/cs/application/
ls
python manage.py dumpdata > csd.json
ls
cd mystudy
ls
vim forms.py
vim models.py
cd ..
python manage.py syncdb
python python loaddata csd.json
ls
python manage.py loaddata csd.json
cat mystudy/forms.py
cat mystudy/models.py
vim mystudy/forms.py
sudo /etc/init.d/apache2 reload
ls
cd tagging/
ls
cat fields
cat fields.py
exit
cd courseslate_d/
ls
rm local*
ls
cd ..
ls
rm -r crs
rm -rf crs
rm -rf csb
cp -r sites/cs/application/ csb
ls
cd courseslate_d/
ls
cp -rf * ../sites/cs/application/
sudo /etc/init.d/apache2 reload
cd ../sites/cs/application/
ls
sudo /etc/init/nginx reload
sudo /etc/init.d/nginx reload
ls
sudo /etc/init.d/apache2 reload
cat settings.py
ls
cat django.wsgi 
sudo /etc/init.d/nginx reload
cd /etc/
ls
cd nginx
ls
ls sites-available/
cat sites-available/courseslate.com 
ls
cat nginx.conf
cd ../apache2/
ls
cat ports.conf 
ls
cat sites-available/
cat sites-available/courseslate.com 
cat sites-available/ropeadopeandwink.com 
cd ~/sites/cs
ls
cd logs
ls
cat error.log 
cd ../application/mystudy/
sudo vim forms.py
cat urls.py
sudo vim views.py
sudo /etc/init.d/apache2 reload
cd ..
python manage.py collectstatic
sudo pip install simplejson
python manage.py collectstatic
python manage.py dumpdata > csd.json
ls
cat csd.json
ls
su postgres
sudo passwd postgres
su postgres
exit
ls
exit
