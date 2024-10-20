%define major     12
%define libname   %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:           intel-gmmlib
Version:        22.5.2
Release:        1
Summary:        Intel Graphics Memory Management Library
Group:          System/Kernel and hardware
License:        MIT and BSD
URL:            https://github.com/intel/gmmlib
Source0:        https://github.com/intel/gmmlib/archive/%{version}/gmmlib-%{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for OpenCL
and the Intel Media Driver for VAAPI.

%package -n     %{libname}
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
%{_libdir}/pkgconfig/igdgmm.pc

%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}

%build
%cmake \
  -DRUN_TEST_SUITE:BOOL=False \
  -DCMAKE_BUILD_TYPE=Release

%make_build

%install
%make_install -C build
find %{buildroot} -name '*.la' -delete
