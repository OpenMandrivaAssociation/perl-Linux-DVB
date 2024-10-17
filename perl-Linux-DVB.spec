%define upstream_name Linux-DVB
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Interface to (some parts of) the Linux DVB API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Linux/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

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
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.10.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 555997
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 552408
- update to 1.01

* Sun Feb 07 2010 Jérôme Brenier <incubusss@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 501534
- import perl-Linux-DVB


* Sun Feb 07 2010 cpan2dist 1.0-1mdv
- initial mdv release, generated with cpan2dist
