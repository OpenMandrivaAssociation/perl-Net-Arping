%define upstream_name    Net-Arping
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Net-Arping module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		perl-Net-Arping-0.02-overflow.patch

BuildRequires:	libnet1.0.2-devel
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
