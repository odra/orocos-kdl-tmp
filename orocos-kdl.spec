Name:       orocos-kdl
Version:    1.3.1
Release:    4%{?dist}
Summary:    A framework for modeling and computation of kinematic chains

License:    LGPLv2+
URL:        http://www.orocos.org/kdl/
%global commit a82743f7cc38e62e942be3f83cc4c2d1cc786021
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source0:    https://github.com/orocos/orocos_kinematics_dynamics/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:     %{name}.ix86-tests.patch

BuildRequires: cmake, eigen3-devel, doxygen, cppunit-devel
BuildRequires: graphviz
Requires:   eigen3

%description
The Kinematics and Dynamics Library (KDL) develops an application independent 
framework for modeling and computation of kinematic chains, such as robots, 
bio-mechanical human models, computer-animated figures, machine tools, etc. 
It provides class libraries for geometrical objects (point, frame, line,... ), 
kinematic chains of various families (serial, humanoid, parallel, mobile,... ),
and their motion specification and interpolation.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.



%prep
%setup -q -n orocos_kinematics_dynamics-%{commit}
%patch0 -p1


%build
pushd orocos_kdl
%cmake \
  -DENABLE_TESTS:BOOL=ON \
  .
make %{?_smp_mflags}
make %{?_smp_mflags} docs
# remove doxygen tag file, it is faulty and we do not need it
rm doc/kdl.tag

popd


%install
pushd orocos_kdl
make install DESTDIR=%{buildroot}
popd


%check
pushd orocos_kdl
make check
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc orocos_kdl/README
%license orocos_kdl/COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_datadir}/orocos_kdl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%doc orocos_kdl/doc/api/html


%changelog
* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 1.3.1-2
- Rebuild for eigen3-3.3.1

* Tue May 03 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.1-1
- Update to 1.3.1
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Sat Jun 27 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-6
- Add upstream patch to fix tests on ix86, reenable ix86
- Add build requirement for graphviz
- Make doc a noarch package
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Tue May 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-4
- Move documentation into doc package
* Thu May 21 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-3
- Exclude arch ix86, because the unit tests fail
* Thu Apr 30 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-2
- Clean up documentation (remove kdl.tag, install html doc)
- Split python bindings into separate SPEC file
* Thu Mar 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-1
- Update to 1.3.0
- Remove libsuffix and version patches (included upstream)
- Enable tests
- Include python subpackage using bootstrapping
* Fri Apr 11 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.2.2-1
- Update to 1.2.2
* Fri Mar 14 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.1.102-2
- Include libsuffix patch
* Fri Feb 14 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.1.102-1
- Initial package
