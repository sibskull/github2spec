Name: 	  $module
Version:  $version
Release:  alt1

Summary:  $summary
License:  $license
Group:    Other
Url: 	  $url

Packager: $packager

Source:   %name-%version.tar

BuildArch: noarch

%description
$description

%prep
%setup

%install
install -Dm 0644 file %buildroot%_bindir/file

%files
%_bindir/*

%changelog
$stamp-alt1
$lastchange
