Name: 	  $module
Version:  $version
Release:  alt1

Summary:  $summary
License:  $license
Group:    Other
Url: 	  $url

Packager: $packager

Source:   %name-%version.tar

BuildRequires:

%description
$description

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README

%changelog
$stamp-alt1
$lastchange
