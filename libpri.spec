#Workaround for 64 bit CPUs
%define _lib lib

Summary: Libpri, an open source implementation of Primary Rate ISDN (PRI)
Name: libpri
Version: 1.4.15
Release: 13%{dist}
License: GPL
Group: Utilities/System
Source: https://downloads.asterisk.org/pub/telephony/libpri/old/libpri-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.asterisk.org
Packager: NethServer <info@nethesis.it>
BuildRequires: dahdi-linux-devel
BuildRequires: dahdi-tools-devel

%description
libpri is a C implementation of the Primary Rate ISDN (PRI) specification.  
It is based on the BellCore specification SR-NWT-002343 for National ISDN.

%package devel
Summary: Libpri libraries and header files for libpri development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The static libraries and header files needed for building additional plugins/modules

%prep
%setup -n %{name}-%{version}

%build
echo %{version} > .version
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version} 
%{__rm} -rf /var/log/jenkins/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_exec_prefix}/lib/libpri.so
%{_exec_prefix}/lib/libpri.so.1.4

%files devel
%defattr(-, root, root)
%{_includedir}/libpri.h
%{_exec_prefix}/lib/libpri.a
