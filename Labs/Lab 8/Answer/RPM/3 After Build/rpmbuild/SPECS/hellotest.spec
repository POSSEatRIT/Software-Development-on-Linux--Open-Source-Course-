Name:           hellotest
Version:        1.1
Release:        1%{?dist}
Summary:        This is the standard hello world program

License:        GPLv2+
URL:            http://ist.rit.edu
Source0:        http://isr.rit.edu/packages/hellotest-1.1.tar.gz

#BuildRequires:  
#Requires:       

%description
Hellotest is a program to print hello world and illustrate how RPMS work. It contains C++ source code and is installed as a command line utility

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc %{_mandir}/man1/hellotest.1.gz
"/usr/sbin/hellotest"
"/usr/share/doc/hellotest /README"


%changelog
* Thu Jan 24 2012 Cody Van De Mark <cav5343@rit.edu> 1.1-1
- This is the initial release
