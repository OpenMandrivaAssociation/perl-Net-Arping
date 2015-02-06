%define upstream_name    Net-Arping
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Net-Arping module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		perl-Net-Arping-0.02-overflow.patch

BuildRequires:	net1.0.2-devel = 1.0.2a-17
BuildRequires:	pcap-devel = 1.3.0-2
BuildRequires:	perl-devel

%description
The module contains function for testing remote host reachability
by sending ARP packets. The program must be run as root or be
setuid.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags}"
# got root?
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 404050
- rebuild using %%perl_convert_version

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.02-10mdv2009.1
+ Revision: 298347
- rebuilt against libpcap-1.0.0

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.02-9mdv2009.0
+ Revision: 257949
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.02-8mdv2009.0
+ Revision: 245998
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.02-6mdv2008.1
+ Revision: 151416
- rebuild for perl-5.10.0

* Fri Jan 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.02-5mdv2008.1
+ Revision: 147964
- added P0 to fix #36669 (Buffer overflow when using perl-Net-Arping-0.02-4mdv2008.0)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02-4mdv2008.0
+ Revision: 18585
- rebuild


* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.02-3mdk
- rebuilt against libnet1.0.2

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.02-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Thu Feb 10 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.02-1mdk
- initial Mandrakelinux package

