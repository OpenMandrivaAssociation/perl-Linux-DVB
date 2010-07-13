%define upstream_name    Linux-DVB
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to (some parts of) the Linux DVB API
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides an interface to the Linux DVB API. It is a
straightforward translation of the C API. You should read the Linux DVB API
description to make any sense of this module. It can be found here:

   http://www.linuxtv.org/docs/dvbapi/dvbapi.html

All constants from _frontend.h_ and _demux.h_ are exported by their C name
and by default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


