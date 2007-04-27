Summary:	Net-Arping module for perl 
Name:		perl-Net-Arping
Version:	0.02
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	Net-Arping-%{version}.tar.bz2
BuildRequires:	libnet1.0.2-devel
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The module contains function for testing remote host reachability
by sending ARP packets. The program must be run as root or be
setuid.

%prep

%setup -q -n Net-Arping-%{version} 

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
