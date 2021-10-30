%define major     11
%define libname   %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:           intel-gmmlib
Version:        21.3.2
Release:        %mkrel 1
Summary:        Intel Graphics Memory Management Library
Group:          System/Kernel and hardware
License:        MIT and BSD
URL:            https://github.com/intel/gmmlib
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# This package relies on intel asm
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for OpenCL
and the Intel Media Driver for VAAPI.

#main package (contains .so.[major]. only)
%package -n     %{libname}
#(!) summary for main lib RPM only
Summary:        Intel Graphics Memory Management Library
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gmmlib.

%package -n     %{develname}
Summary:        Headers for developing programs that will use gmmlib
Group:          Development/C++
Requires:       %{libname} = %{version}
#(!) MANDATORY
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gmmlib.

%files -n %{libname}
%{_libdir}/libigdgmm.so.%{major}{,.*}

%files -n %{develname}
%doc README.rst
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
# We don't use the static library
%exclude %{_libdir}/libgmm_umd.a
%{_libdir}/pkgconfig/igdgmm.pc


%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
# Fix license perm
chmod -x LICENSE.md README.rst
# Fix source code perm
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'


%build
%cmake \
  -DRUN_TEST_SUITE:BOOL=False

%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.la' -delete
