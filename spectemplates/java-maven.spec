
Name:           $module
Version:        $version
Release:        alt1
Summary:        $summary

Group:          Development/Java
License:        $license
URL:            $url
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-maven-local
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  maven

BuildArch:	noarch
Requires:       java >= 1.6.0
Requires:       jpackage-utils

%description
$description

%package javadoc
Summary:        Javadoc for %name
Group:          Documentation
Requires:       jpackage-utils
BuildArch:      noarch

Requires:       jpackage-utils
Requires:       %name = %version-%release

%description javadoc
Javadoc for %name.

%prep
%setup

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar \
                 %buildroot%_javadir/%{name}.jar

# pom
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-%name.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr target/site/api*/* %buildroot%_javadocdir/%name/

%files
%doc README.txt LICENSE.txt
%_javadir/*
%_mavenpomdir/*
%_mavendepmapfragdir/*

%files javadoc
%doc LICENSE.txt
%doc %_javadocdir/%name

%changelog
$stamp-alt1
$lastchange
